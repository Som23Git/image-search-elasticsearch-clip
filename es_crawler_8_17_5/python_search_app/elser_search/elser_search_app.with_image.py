from flask import Flask, request, render_template, jsonify
from elasticapm.contrib.flask import ElasticAPM
from elasticsearch import Elasticsearch
from math import ceil
import json
import logging

# Import config
import config

app = Flask(__name__)

# Enabling Elasticsearch debug logs
logging.basicConfig(level=logging.DEBUG)

# Elastic APM configuration
app.config['ELASTIC_APM'] = {
    'SERVICE_NAME': config.APM_SERVICE_NAME,
    'SERVER_URL': config.APM_SERVER_URL,
    'SECRET_TOKEN': config.APM_SECRET_TOKEN,
    'DEBUG': True
}
apm = ElasticAPM(app)

# Elasticsearch connection
es = Elasticsearch(
    config.ELASTIC_CLOUD_URL,
    api_key=config.ELASTIC_API_KEY
)

# Health check route
@app.route('/')
def health_check():
    return jsonify({"status": "healthy"}), 200

@app.route('/test_apm')
def test_apm():
    apm.capture_message('APM test message from /test_apm')
    return jsonify({"status": "APM test sent!"})

# Elser Search Route
@app.route('/elser_search', methods=['GET', 'POST'])
def elser_search():
    results = []
    total = 0
    page = int(request.args.get('page', 1))
    size = 10
    total_pages = 0
    search_term = ""

    if request.method == 'POST':
        search_term = request.form.get('query', '')
        from_ = (page - 1) * size

        # Elasticsearch Search Application request
        response = es.transport.perform_request(
            "POST",
            f"/_application/search_application/{config.SEARCH_APPLICATION_NAME}/_search",
            body={
                "params": {
                    "query": search_term,
                    "search_fields": ["title", "directions"],
                    "from": from_,
                    "size": size
                }
            },
            headers={
                "Content-Type": "application/json",
                "Authorization": f"ApiKey {config.ELASTIC_API_KEY}"
            }
        )

        # Pretty print full response (optional for debugging)
        print(json.dumps(response.body, indent=2))

        # Extract data
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
        'search.with_image.html',
        results=results,
        total=total,
        page=page,
        total_pages=total_pages,
        query=search_term
    )

if __name__ == '__main__':
    app.run(debug=True)
