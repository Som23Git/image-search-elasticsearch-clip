import json
from flask import Flask
from elasticsearch import Elasticsearch
from PIL import Image
from transformers import CLIPProcessor, CLIPModel
import torch
import numpy as np
from io import BytesIO
import requests
from pprint import pprint

# Import config
import config

# Flask app
app = Flask(__name__)

# Elasticsearch client
es = Elasticsearch(
    config.ELASTIC_URL,
    api_key=config.ELASTIC_API_KEY
)

# CLIP model setup
device = "cuda" if torch.cuda.is_available() else "cpu"
model = CLIPModel.from_pretrained(config.CLIP_MODEL_NAME).to(device)
processor = CLIPProcessor.from_pretrained(config.CLIP_MODEL_NAME)

# Function to generate image embeddings
def generate_embedding(image_url):
    try:
        response = requests.get(image_url)
        response.raise_for_status()

        image = Image.open(BytesIO(response.content)).convert("RGB")
        inputs = processor(images=image, return_tensors="pt").to(device)

        with torch.no_grad():
            outputs = model.get_image_features(**inputs)

        embedding = outputs / outputs.norm(p=2, dim=-1, keepdim=True)
        embedding_np = embedding.cpu().numpy().flatten()

        print(f"Embedding generated with shape: {embedding_np.shape}")
        print("First 10 embedding values:", embedding_np[:10])  # For clarity

        return embedding_np.tolist()

    except Exception as e:
        print(f"Error generating embedding: {str(e)}")
        return None

# Perform the search using the search template
def search_image(image_url):
    vector = generate_embedding(image_url)

    if vector is None:
        print("Skipping search due to embedding error.")
        return

    if len(vector) != 512:
        print(f"Embedding is not 512 dimensions: {len(vector)}")
        return

    print("Embedding is 512 dimensions.")
    print("Searching similar images in Elasticsearch...")

    try:
        response = es.transport.perform_request(
            "POST",
            f"{config.ELASTIC_URL}/search-testing-v7/_search/template",  
            body={
                "id": config.IMAGE_SEARCH_TEMPLATE,
                "params": {
                    "knn_field": "image_embedding",
                    "query_vector": vector,
                    "k": config.KNN_K,
                    "num_candidates": config.KNN_NUM_CANDIDATES,
                    "fields": config.KNN_FIELDS
                },
            },
            headers={
                "Authorization": f"ApiKey {config.ELASTIC_API_KEY}",
                "Content-Type": "application/json"
            }
        )

        print("Raw Elasticsearch response:")
        pprint(response)

    except Exception as e:
        print(f"Error querying Elasticsearch: {str(e)}")

# Run the search
if __name__ == '__main__':
    search_image(config.EXAMPLE_IMAGE_URL)
    app.run(debug=True)