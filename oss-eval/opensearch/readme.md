Opensearch Benchmark:

https://opensearch.org/blog/opensearch-3-0-enhances-vector-database-performance/


Github: https://github.com/opensearch-project/OpenSearch/releases/tag/3.0.0

Image used: https://hub.docker.com/layers/opensearchproject/opensearch/3.0.0/images/sha256-22c18a39aae9868d76df4ffc4713d164c81b2c5ee8be7ad67da96e0ecd5212e0

docker pull opensearchproject/opensearch:3.0.0

https://github.com/opensearch-project/OpenSearch/releases/tag/3.0.0

docker search opensearch

docker run -d --name opensearch-3 \
  -p 9200:9200 -p 9600:9600 \
  -e "discovery.type=single-node" \
  -e "plugins.security.disabled=true" \
  opensearchproject/opensearch:3.0.0

docker run --name opensearch-dashboards-3 \
  -p 5601:5601 \
  -e "OPENSEARCH_HOSTS=http://host.docker.internal:9200" \
  opensearchproject/opensearch-dashboards:3.0.0


docker run --name opensearch-3 \
  -p 9200:9200 -p 9600:9600 \
  -e "discovery.type=single-node" \
  -e "plugins.security.disabled=true" \
  -e "OPENSEARCH_INITIAL_ADMIN_PASSWORD=pfQ4'7X2@u0" \
  opensearchproject/opensearch:3.0.0


docker run --name opensearch-3 --network opensearch-net \
  -p 9200:9200 -p 9600:9600 \
  -e "discovery.type=single-node" \
  -e "OPENSEARCH_INITIAL_ADMIN_PASSWORD=pfQ4'7X2@u0" \
  opensearchproject/opensearch:3.0.0


docker run -d --name opensearch-dashboards-3 --network opensearch-net \
  -p 5601:5601 \
  -e "OPENSEARCH_HOSTS=http://host.docker.internal:9200" \
  opensearchproject/opensearch-dashboards:3.0.0


curl -XPOST -u admin:pfQ4'7X2@u0 https://localhost:9200/_plugins/_ml/models/_register \
-H "Content-Type: application/json" -k \
-d '{
  "name": "all-MiniLM-L6-v2",
  "version": "1.0.1",
  "description": "Lightweight semantic search model",
  "model_format": "TORCH_SCRIPT",
  "model_config": {
    "model_type": "bert",
    "embedding_dimension": 384,
    "framework_type": "sentence_transformer"
  },
  "url": "https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/pytorch_model.bin"
}'
