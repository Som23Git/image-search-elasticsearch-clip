# OpenSearch 3.0.0 

## Quickstart & Feature Comparison with Elasticsearch

OpenSearch is a community-driven, `Apache 2.0-licensed` open-source search and analytics suite, originally derived from Elasticsearch 7.10.2.

---

## Benchmark

Read the official benchmark report from the OpenSearch team:
https://opensearch.org/blog/opensearch-3-0-enhances-vector-database-performance/

---

## User Experience

Feels very old fashioned, not updated but, they do have some good features that are exposed like `notebooks, AI workflows` to tryout the visualization and the code.

When trying to install or add LLM models, it's more of a manual work using the APIs, as for now they support `API only`.

Attaching the postman collection for deploying the models.

Please note, it got its own `good search features`, and `average observability` and `less security` features.

---
## Version

- Release Tag: [v3.0.0](https://github.com/opensearch-project/OpenSearch/releases/tag/3.0.0)
- Docker Image: [opensearchproject/opensearch:3.0.0](https://hub.docker.com/layers/opensearchproject/opensearch/3.0.0/images/sha256-22c18a39aae9868d76df4ffc4713d164c81b2c5ee8be7ad67da96e0ecd5212e0)
- Maven Artifacts: https://mvnrepository.com/artifact/org.opensearch/opensearch/3.0.0

---

## Key Differences: OpenSearch vs Elasticsearch

| Feature                  | **OpenSearch**                          | **Elasticsearch**                          |
|--------------------------|------------------------------------------|--------------------------------------------|
| **License**              | Apache 2.0 (open-source)                | Elastic License / SSPL (proprietary)       |
| **Security (TLS, RBAC)** | ✅ Free and built-in                    | ✅ Free but under Elastic license           |
| **Dashboards UI**        | OpenSearch Dashboards                   | Kibana                                     |
| **Query Language**       | SQL, PPL                                | SQL, EQL                                   |
| **Machine Learning**     | Anomaly detection (free)                | Advanced ML (paid)                         |
| **Vector Search**        | KNN plugin, native support              | `dense_vector`, Elser (partial + paid)     |
| **Alerting**             | ✅ Free plugin                          | Paid feature                                |
| **Multi-Tenancy**        | ✅ Yes                                   | ❌ No                                       |
| **Reporting**            | ✅ Free                                   | ❌ Paid feature                             |
| **Plugin Support**       | ✅ Open and extensible                   | ❌ Open and Source available(ELv2)                     |
| **Cloud Service**        | AWS OpenSearch (Serverless available)   | Elastic Cloud (Serverless recently GA)                         |
| **Governance**           | Community + AWS (open roadmap)          | Elastic controls roadmap   |

---

## Docker Quickstart

### Pull OpenSearch 3.0.0 Image(Latest, announced this May, 2025)

```bash
docker pull opensearchproject/opensearch:3.0.0
```

---

### Run OpenSearch (Single Node)

```bash
docker run --name opensearch-3 \
  -p 9200:9200 -p 9600:9600 \
  -e "discovery.type=single-node" \
  -e "plugins.security.disabled=true" \
  opensearchproject/opensearch:3.0.0
```

Or with security enabled:

```bash
docker run --name opensearch-3 \
  -p 9200:9200 -p 9600:9600 \
  -e "discovery.type=single-node" \
  -e "OPENSEARCH_INITIAL_ADMIN_PASSWORD=pfQ4'7X2@u0" \
  opensearchproject/opensearch:3.0.0
```

---

### Run OpenSearch Dashboards(which is Kibana)

```bash
docker run --name opensearch-dashboards-3 \
  -p 5601:5601 \
  -e "OPENSEARCH_HOSTS=http://host.docker.internal:9200" \
  opensearchproject/opensearch-dashboards:3.0.0
```

Or on a custom network:

```bash
docker network create opensearch-net

docker run --name opensearch-3 --network opensearch-net \
  -p 9200:9200 -p 9600:9600 \
  -e "discovery.type=single-node" \
  -e "OPENSEARCH_INITIAL_ADMIN_PASSWORD=pfQ4'7X2@u0" \
  opensearchproject/opensearch:3.0.0

docker run -d --name opensearch-dashboards-3 --network opensearch-net \
  -p 5601:5601 \
  -e "OPENSEARCH_HOSTS=http://opensearch-3:9200" \
  opensearchproject/opensearch-dashboards:3.0.0
```

---

## 🤖 Register a Vector Model

Register a lightweight sentence transformer (MiniLM) using OpenSearch ML plugin:

```bash
curl -XPOST -u admin:openSearchPassword@123 https://localhost:9200/_plugins/_ml/models/_register \
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
```

---

## Additional References

* 🔗 [OpenSearch Blog: Vector DB Benchmarks](https://opensearch.org/blog/opensearch-3-0-enhances-vector-database-performance/)
* 📦 [OpenSearch Docker Hub](https://hub.docker.com/r/opensearchproject/opensearch)
* 🧪 [GitHub Releases](https://github.com/opensearch-project/OpenSearch/releases)
* 📄 [Maven License Artifacts for Opensearch 3.0.0(latest)](https://mvnrepository.com/artifact/org.opensearch/opensearch/3.0.0)

---