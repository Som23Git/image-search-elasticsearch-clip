# This is a search application which I created to use Elser Search 
# directly using the querying the search-testing-v7 index directly

from flask import Flask, request, render_template, jsonify
from elasticsearch import Elasticsearch
from math import ceil
from elasticapm.contrib.flask import ElasticAPM

import logging
import config  

app = Flask(__name__)
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
    cloud_id=config.ELASTIC_CLOUD_ID,
    api_key=config.ELASTIC_API_KEY
)

# Health check
@app.route('/')
def health_check():
    return jsonify({"status": "healthy"}), 200

@app.route('/test_apm')
def test_apm():
    apm.capture_message('APM test message from /test_apm')
    return jsonify({"status": "APM test sent!"})

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
                                    "model_id": config.ELSER_MODEL_ID,
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
            "Authorization": f"ApiKey {config.ELASTIC_API_KEY}"
        }

        status, response_body = es.transport.perform_request(
            "POST",
            f"/{config.ELASTIC_INDEX}/_search",
            headers=headers,
            body=query
        )

        total = response_body['hits']['total']['value']
        total_pages = ceil(total / size)
        results = [
            {**hit['_source'], '_score': hit['_score']}
            for hit in response_body['hits']['hits']
        ]

    return render_template(
        'search.beta.html',
        results=results,
        total=total,
        page=page,
        total_pages=total_pages
    )

if __name__ == '__main__':
    app.run(debug=False)