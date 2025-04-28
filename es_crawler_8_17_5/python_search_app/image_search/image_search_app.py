######
# Following the issue:
# /python_testing_search_appln/image_search_app.bug
# known bug: https://github.com/elastic/elasticsearch/issues/116246
# https://discuss.elastic.co/t/search-application-mustache-template-issue-when-passing-floats-vs-integers/376062/2
# "type": "null_pointer_exception",
# "reason": """Cannot invoke "com.fasterxml.jackson.core.JsonLocation.getLineNr()" because "loc" is null"""
######


####################################
# Using SEARCH TEMPLATES Directly
# reference documentation: https://www.elastic.co/docs/solutions/search/search-templates#create-search-template
####################################

import json
from flask import Flask
from elasticsearch import Elasticsearch
from PIL import Image
from transformers import CLIPProcessor, CLIPModel
import torch
import numpy as np
from io import BytesIO
import requests

# Import config
import config

# Flask app
app = Flask(__name__)

# Define config variables locally
ELASTIC_URL = config.ELASTIC_URL
API_KEY = config.ELASTIC_API_KEY
INDEX_NAME = config.INDEX_NAME
IMAGE_SEARCH_TEMPLATE = config.IMAGE_SEARCH_TEMPLATE
CLIP_MODEL_NAME = config.CLIP_MODEL_NAME
KNN_FIELD = config.KNN_FIELD
KNN_K = config.KNN_K
KNN_NUM_CANDIDATES = config.KNN_NUM_CANDIDATES
KNN_FIELDS = config.KNN_FIELDS

# Elasticsearch client
es = Elasticsearch(ELASTIC_URL, api_key=API_KEY)

# CLIP model setup
device = "cuda" if torch.cuda.is_available() else "cpu"
model = CLIPModel.from_pretrained(CLIP_MODEL_NAME).to(device)
processor = CLIPProcessor.from_pretrained(CLIP_MODEL_NAME)

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
        # printing it for clarity whether the embeddings are generated or NOT
        print("First 10 embedding values:", embedding_np[:10])

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
        # Elasticsearch search template using the correct path
        response = es.transport.perform_request(
            "POST",
            f"{ELASTIC_URL}/search-testing-v7/_search/template",
            body={
                "id": "image_search_template", 
                "params": {
                    "knn_field": KNN_FIELD,
                    "query_vector": vector,
                    "k": KNN_K,
                    "num_candidates": KNN_NUM_CANDIDATES,
                    "fields": KNN_FIELDS
                }
            },
            headers={
                "Authorization": f"ApiKey {API_KEY}",
                "Content-Type": "application/json"
            }
        )

        # Parse and print filtered Elasticsearch response
        response_body = response.body
        hits = response_body.get("hits", {}).get("hits", [])

        print("Elasticsearch response (filtered fields):")
        for hit in hits:
            source = hit["_source"]
            filtered_data = {
                "title": source.get("title", "N/A"),
                "directions": source.get("directions", "N/A"),
                "ingredients": source.get("ingredients", "N/A"),
                "image": source.get("image", "N/A"),
                "score": hit.get("_score", "N/A")
            }
            print(json.dumps(filtered_data, indent=2))

    except Exception as e:
        print(f"Error querying Elasticsearch: {str(e)}")

# Get the image URL as input
if __name__ == '__main__':
    image_url = input("Please enter the image URL for searching: ")
    search_image(image_url)
    app.run(debug=True)