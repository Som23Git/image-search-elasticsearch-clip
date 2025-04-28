import json
from flask import Flask, request, render_template
from elasticsearch import Elasticsearch
from math import ceil
from PIL import Image
from transformers import CLIPProcessor, CLIPModel

from io import BytesIO
import requests
import torch
import config

from elasticapm.contrib.flask import ElasticAPM

# Assigning config variables
ELASTIC_URL = config.ELASTIC_URL
ELASTIC_API_KEY = config.ELASTIC_API_KEY
INDEX_NAME = config.INDEX_NAME
SEARCH_APPLICATION_NAME = config.SEARCH_APPLICATION_NAME
IMAGE_SEARCH_TEMPLATE = config.IMAGE_SEARCH_TEMPLATE
CLIP_MODEL_NAME = config.CLIP_MODEL_NAME
KNN_K = config.KNN_K
KNN_NUM_CANDIDATES = config.KNN_NUM_CANDIDATES
SEARCH_FIELDS = config.KNN_SEARCH_FIELDS
KNN_FIELD = config.KNN_FIELD

# Flask app
app = Flask(__name__)

app.config['ELASTIC_APM'] = {
    'SERVICE_NAME': config.APM_SERVICE_NAME,
    'SERVER_URL': config.APM_SERVER_URL,
    'SECRET_TOKEN': config.APM_SECRET_TOKEN,
    'ENVIRONMENT': config.APM_APP_ENVIRONMENT
}

apm = ElasticAPM(app)

# Elasticsearch connection
es = Elasticsearch(
    ELASTIC_URL,
    api_key=ELASTIC_API_KEY
)

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
        print("First 10 embedding values:", embedding_np[:10])

        return embedding_np.tolist()

    except Exception as e:
        print(f"Error generating embedding: {str(e)}")
        return None

def search_image_by_vector(vector):
    if vector is None or len(vector) != 512:
        print("Invalid vector passed to search.")
        return []

    try:
        response = es.transport.perform_request(
            "POST",
            f"/{INDEX_NAME}/_search/template",
            body={
                "id": IMAGE_SEARCH_TEMPLATE,
                "params": {
                    "knn_field": KNN_FIELD,
                    "query_vector": vector,
                    "k": KNN_K,
                    "num_candidates": KNN_NUM_CANDIDATES,
                    "fields": SEARCH_FIELDS
                }
            },
            headers={
                "Authorization": f"ApiKey {ELASTIC_API_KEY}",
                "Content-Type": "application/json"
            }
        )

        hits = response.body.get("hits", {}).get("hits", [])
        results = []
        for hit in hits:
            source = hit["_source"]
            results.append({
                "title": source.get("title", "N/A"),
                "directions": source.get("directions", "N/A"),
                "ingredients": source.get("ingredients", "N/A"),
                "image": source.get("image", "N/A"),
                "url": source.get("url", "#"),
                "_score": hit.get("_score", "N/A")
            })
        return results

    except Exception as e:
        print(f"Error in vector-based image search: {str(e)}")
        return []

@app.route('/')
def home():
    return render_template('/image_plus_elser_app/home.html',rum_service_name=config.RUM_SERVICE_NAME,
        rum_server_url=config.RUM_SERVER_URL,
        rum_environment=config.RUM_ENVIRONMENT
)

@app.route('/image_search', methods=['GET','POST'])
def image_search():
    image_results = []
    image_url = request.form.get("image_url")
    image_file = request.files.get("image")

    if image_file:
        image = Image.open(image_file.stream).convert("RGB")
        inputs = processor(images=image, return_tensors="pt").to(device)
        with torch.no_grad():
            outputs = model.get_image_features(**inputs)
        embedding = outputs / outputs.norm(p=2, dim=-1, keepdim=True)
        vector = embedding.cpu().numpy().flatten().tolist()
        image_results = search_image_by_vector(vector)
    elif image_url:
        vector = generate_embedding(image_url)
        image_results = search_image_by_vector(vector)

    return render_template('/image_plus_elser_app/image_search.html', image_results=image_results, rum_service_name=config.RUM_SERVICE_NAME,
        rum_server_url=config.RUM_SERVER_URL,
        rum_environment=config.RUM_ENVIRONMENT
)

### The pagination is NOT handled in this "elser_search" block ####
# @app.route('/elser_search', methods=['GET', 'POST'])
# def elser_search():
#     results = []
#     total = 0
#     page = int(request.args.get('page', 1))
#     size = 10
#     total_pages = 0
#     search_term = ""

#     if request.method == 'POST':
#         search_term = request.form.get('query', '')
#         from_ = (page - 1) * size

#         response = es.transport.perform_request(
#             "POST",
#             f"/_application/search_application/{SEARCH_APPLICATION_NAME}/_search",
#             body={
#                 "params": {
#                     "query": search_term,
#                     "search_fields": ["title", "directions"],
#                     "from": from_,
#                     "size": size
#                 }
#             },
#             headers={
#                 "Content-Type": "application/json",
#                 "Authorization": f"ApiKey {ELASTIC_API_KEY}"
#             }
#         )

#         total = response.body['hits']['total']['value']
#         total_pages = ceil(total / size)
#         results = [
#             {
#                 **hit['_source'],
#                 '_score': hit['_score']
#             }
#             for hit in response.body['hits']['hits']
#         ]

#     return render_template(
#         '/image_plus_elser_app/elser_search.html',
#         results=results,
#         total=total,
#         page=page,
#         total_pages=total_pages,
#         query=search_term
#     )

## Handled Pagination here but, it does not scroll through the results instead shares the same results
@app.route('/elser_search', methods=['GET', 'POST'])
def elser_search():
    results = []
    total = 0
    page = int(request.args.get('page', 1))
    size = 10
    total_pages = 0

    # Handle both POST and GET for the search term
    if request.method == 'POST':
        search_term = request.form.get('query', '')
    else:
        search_term = request.args.get('query', '')  ## Using this to talk to the html pagination query

    if search_term:
        from_ = (page - 1) * size

        response = es.transport.perform_request(
            "POST",
            f"/_application/search_application/{SEARCH_APPLICATION_NAME}/_search",
            body={
                "params": {
                    "query": search_term,
                    "search_fields": ["title", "directions"],
                    "from": from_,
                    "size": size
                },
            },
            headers={
                "Content-Type": "application/json",
                "Authorization": f"ApiKey {ELASTIC_API_KEY}"
            }
        )

        total = response.body['hits']['total']['value']
        total_pages = ceil(total / size)
        results = [
            {
                **hit['_source'],
                '_score': hit['_score']
            }
            for hit in response.body['hits']['hits']
        ]

    return render_template(
        '/image_plus_elser_app/elser_search.html',
        results=results,
        total=total,
        page=page,
        total_pages=total_pages,
        query=search_term,
        rum_service_name=config.RUM_SERVICE_NAME,
        rum_server_url=config.RUM_SERVER_URL,
        rum_environment=config.RUM_ENVIRONMENT
    )

if __name__ == '__main__':
    app.run(debug=False)
