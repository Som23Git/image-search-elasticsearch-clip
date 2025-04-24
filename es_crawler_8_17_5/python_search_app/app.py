from flask import Flask, request, render_template
from elasticsearch import Elasticsearch
import logging
import base64

app = Flask(__name__)

# Enable Elasticsearch debug logs at the very start
logging.basicConfig(level=logging.DEBUG)

# Elasticsearch connection
es = Elasticsearch(
    cloud_id="elasticTestingDeployment:dXMtY2VudHJhbDEuZ2NwLmNsb3VkLmVzLmlvOjQ0MyQ1ZWFjZDhmNTk0M2U0OTAyYWZlOTcyYzI0MGYwOGJlMSRlOWExZGU1NWExZjQ0YmJlOTQ5YmQxZjIwZTVjY2RhYQ==",
    api_key="alNvUWFaWUJpd01WVUl2YUJ3eEs6TE5Hb1pVR0hSbXlMN3gyVU1Ea2JLUQ=="
)

# Confirm Elasticsearch endpoint
# print("Elasticsearch Info:", es.info())

@app.route('/', methods=['GET', 'POST'])
def search():
    results = []
    if request.method == 'POST':
        search_term = request.form['query']
        
        # Elasticsearch query with text_expansion
        query = {
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

        # Prepare authentication header (manual for perform_request)
        api_key = "alNvUWFaWUJpd01WVUl2YUJ3eEs6TE5Hb1pVR0hSbXlMN3gyVU1Ea2JLUQ=="
        # encoded_api_key = base64.b64encode(api_key.encode()).decode()

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"ApiKey {api_key}"
        }

        # Send raw request
        status, response_body = es.transport.perform_request(
            "POST",
            "/search-testing-v4/_search",
            headers=headers,
            body=query
        )

        print("Response Body:", response_body)

        if "hits" in response_body:
            results = [hit['_source'] for hit in response_body['hits']['hits']]
        else:
            results = []

    return render_template('search.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)