from flask import Flask, request, render_template, jsonify
from elasticsearch import Elasticsearch
import logging
from math import ceil
from elasticapm.contrib.flask import ElasticAPM

app = Flask(__name__)

# Enable Elasticsearch debug logs
logging.basicConfig(level=logging.DEBUG)

# Elastic APM configuration
app.config['ELASTIC_APM'] = {
    'SERVICE_NAME': 'recipe-search-app',
    'SERVER_URL': 'https://1cf8e211c1bf484489b37841ceebdeb3.apm.us-central1.gcp.cloud.es.io:443',
    'SECRET_TOKEN': 'bMokHCGAKV9fkeaGG0',
    'DEBUG': True
    # Optional: 'ENVIRONMENT': 'development',
}

apm = ElasticAPM(app)

# Elasticsearch connection
es = Elasticsearch(
    cloud_id="elasticTestingDeployment:dXMtY2VudHJhbDEuZ2NwLmNsb3VkLmVzLmlvOjQ0MyQ1ZWFjZDhmNTk0M2U0OTAyYWZlOTcyYzI0MGYwOGJlMSRlOWExZGU1NWExZjQ0YmJlOTQ5YmQxZjIwZTVjY2RhYQ==",
    api_key="alNvUWFaWUJpd01WVUl2YUJ3eEs6TE5Hb1pVR0hSbXlMN3gyVU1Ea2JLUQ=="
)

# Health check route
@app.route('/')
def health_check():
    return jsonify({"status": "healthy"}), 200

@app.route('/test_apm')
def test_apm():
    apm.capture_message('APM test message from /test_apm')
    return jsonify({"status": "APM test sent!"})

# ELSER search route
@app.route('/elser_search', methods=['GET', 'POST'])
def elser_search():
    results = []
    total = 0
    page = int(request.args.get('page', 1))
    size = 10
    total_pages = 0

    if request.method == 'POST':
        search_term = request.form['query']
        from_ = (page - 1) * size

        query = {
            "from": from_,
            "size": size,
            "query": {
                "bool": {
                    "should": [
                        {
                            "text_expansion": {
                                "ml.inference.directions_expanded.predicted_value": {
                                    "model_id": ".elser_model_2_linux-x86_64",
                                    "model_text": search_term
                                }
                            }
                        }
                    ]
                }
            },
            "_source": ["title", "directions", "ingredients", "url"]
        }

        headers = {
            "Content-Type": "application/json",
            "Authorization": "ApiKey alNvUWFaWUJpd01WVUl2YUJ3eEs6TE5Hb1pVR0hSbXlMN3gyVU1Ea2JLUQ=="
        }

        status, response_body = es.transport.perform_request(
            "POST",
            "/search-testing-v4/_search",
            headers=headers,
            body=query
        )

        print("Response Body:", response_body)

        total = response_body['hits']['total']['value']
        total_pages = ceil(total / size)
        results = [
            {
                **hit['_source'],
                '_score': hit['_score']
            }
            for hit in response_body['hits']['hits']
        ]

    return render_template(
        'search.html',
        results=results,
        total=total,
        page=page,
        total_pages=total_pages
    )

if __name__ == '__main__':
    app.run(debug=False)
