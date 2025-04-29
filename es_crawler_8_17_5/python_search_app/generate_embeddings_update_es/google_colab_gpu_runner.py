"""
Async Embedding Updater for Elasticsearch
-------------------------------------------
Author: Som
Project: Behavioral Analytics Testing
Time Taken: ~1 hour
Environment: Google Colab [T4 GPU Runtime] for Faster Processing

Description:
- Downloads images from given URLs in a CSV file
- Generates 512D embeddings using OpenAI CLIP model
- Updates corresponding documents in an Elasticsearch index
- Uses asyncio + aiohttp for fast concurrent processing
- Skips rows with invalid URLs, failed downloads, or embedding errors

Tested on: Google Colab, 2024-04-29
"""

import pandas as pd
import aiohttp
import asyncio
import torch
from transformers import CLIPProcessor, CLIPModel
from elasticsearch import Elasticsearch
from PIL import Image
from io import BytesIO
from tqdm import tqdm
import requests
import os
import config

# --- Configuration ---
CSV_FILE = config.CSV_FILE
INDEX_NAME = config.INDEX_NAME
ES_URL = config.ES_URL
ES_API_KEY = config.ES_API_KEY

BATCH_SIZE = config.BATCH_SIZE
CONCURRENT_TASKS = config.CONCURRENT_TASKS

# --- Elasticsearch Connection ---
es = Elasticsearch(ES_URL, api_key=ES_API_KEY)

# --- CLIP Model Setup ---
device = "cuda" if torch.cuda.is_available() else "cpu"
model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32").to(device)
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

# --- Async Session ---
session = None

# --- CSV Loading ---
df = pd.read_csv(CSV_FILE)
if 'status' not in df.columns:
    df['status'] = ''

print("Available columns:", df.columns.tolist())

# --- Helper Functions ---
# async def download_image(url):
#     try:
#         async with session.get(url) as response:
#             if response.status == 200:
#                 return await response.read()
#             else:
#                 return None
#     except Exception as e:
#         print(f"[Download Error] {url}: {e}")
#         return None

async def download_image(url):
    try:
        timeout = aiohttp.ClientTimeout(total=15)  # Timeout 15 seconds PER IMAGE
        async with session.get(url, timeout=timeout) as response:
            if response.status == 200:
                return await response.read()
            else:
                print(f"[Download] Failed: {url} Status: {response.status}")
                return None
    except asyncio.TimeoutError:
        print(f"[Timeout] Image download timeout for {url}")
        return None
    except Exception as e:
        print(f"[Download error] {url}: {e}")
        return None

def generate_embedding(image_bytes):
    try:
        image = Image.open(BytesIO(image_bytes)).convert("RGB")
        inputs = processor(images=image, return_tensors="pt").to(device)

        with torch.no_grad():
            outputs = model.get_image_features(**inputs)

        embedding = outputs / outputs.norm(p=2, dim=-1, keepdim=True)
        return embedding.cpu().numpy().flatten().tolist()
    except Exception as e:
        print(f"[Embedding Error] {e}")
        return None

async def process_row(index, row):
    doc_id = row['_id']
    image_url = row['image']

    print(f"[Pick] Document: {doc_id} | Image URL: {image_url}")

    if not isinstance(image_url, str) or not image_url.startswith('http'):
        print(f"[Skip] Invalid URL for document {doc_id}. Skipping.")
        return 'invalid-url'

    image_bytes = await download_image(image_url)
    if image_bytes is None:
        print(f"[Error] Failed to download image for document {doc_id}.")
        return 'download-failed'

    embedding = generate_embedding(image_bytes)
    if embedding is None:
        print(f"[Error] Failed to generate embedding for document {doc_id}.")
        return 'embedding-failed'

    try:
        es.update(
            index=INDEX_NAME,
            id=doc_id,
            body={
                "doc": {
                    "image_embedding": embedding
                }
            }
        )
        print(f"[Success] ✅ Updated document: {doc_id}")
        return 'success'
    except Exception as e:
        print(f"[Error] Elasticsearch update failed for document {doc_id}: {e}")
        return 'es-update-failed'

async def worker(sem, index, row):
    async with sem:
        status = await process_row(index, row)
        df.at[index, 'status'] = status

async def main():
    global session
    connector = aiohttp.TCPConnector(limit_per_host=CONCURRENT_TASKS)
    timeout = aiohttp.ClientTimeout(total=60)
    session = aiohttp.ClientSession(connector=connector, timeout=timeout)

    sem = asyncio.Semaphore(CONCURRENT_TASKS)
    tasks = []
    counter = 0

    with tqdm(total=len(df)) as pbar:
        for idx, row in df.iterrows():
            if row['status'] == 'success':
                pbar.update(1)
                continue

            task = asyncio.create_task(worker(sem, idx, row))
            tasks.append(task)

            if len(tasks) >= BATCH_SIZE:
                await asyncio.gather(*tasks)
                df.to_csv(CSV_FILE, index=False)
                tasks = []

            counter += 1
            pbar.update(1)

        if tasks:
            await asyncio.gather(*tasks)
            df.to_csv(CSV_FILE, index=False)

    await session.close()

if __name__ == "__main__":
    import nest_asyncio
    nest_asyncio.apply()
    asyncio.get_event_loop().run_until_complete(main())