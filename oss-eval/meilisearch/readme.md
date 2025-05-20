# Meilisearch Local Setup — Fast, Typo-Tolerant Search

![meilisearch_instance](./assets/meilisearch_instance.png)

Meilisearch is a **blazing-fast**, open-source, typo-tolerant search engine built in **Rust**, designed to deliver great search experiences with minimal configuration.

This repository documents a local Meilisearch setup, including:
- Local Docker-based deployment
- Custom vector search
- Hybrid semantic search with filters and sorting
- File structure breakdown
- Postman collection for easy testing

---

## Quick Links

- [Meilisearch Cloud](https://www.meilisearch.com/cloud?utm_campaign=oss&utm_source=engine&utm_medium=cli)
- [Documentation](https://www.meilisearch.com/docs)
- [Source Code (GitHub)](https://github.com/meilisearch/meilisearch)
- [Discord Community](https://discord.meilisearch.com)
- License: MIT - No Copy-left restrictions
- [Meilisearch vs Elasticsearch](https://www.meilisearch.com/blog/meilisearch-vs-elasticsearch)

---

## Local Setup Overview

![meilisearch_local_setup](./assets/meilisearch_local_setup.png)

### Setup Components

- `meilisearch` container (search backend)
- Optional UI (e.g., [riccoxie/meilisearch-ui](https://github.com/riccox/meilisearch-ui))
- Vector search using user-provided embeddings
- Semantic hybrid search with filters/sorting

---

## Storage Structure

Here’s the `meili_data` directory layout after running Meilisearch locally with persistent volumes:

```
meili_data/
├── data.ms
│ ├── VERSION
│ ├── auth/
│ ├── indexes/
│ ├── instance-uid
│ ├── tasks/
│ └── update_files/
└── dumps/
```

### Storage Breakdown

| Path                    | Purpose                              |
| ----------------------- | ------------------------------------ |
| `data.ms/auth`          | Auth tokens & API keys               |
| `data.ms/indexes/`      | Full-text & vector index data        |
| `data.ms/tasks/`        | Task queue tracking                  |
| `data.ms/update_files/` | Temp staging for updates             |
| `data.ms/instance-uid`  | Unique instance identifier           |
| `dumps/`                | Snapshots and backups (via API)      |

Powered by **LMDB (Lightning Memory-Mapped Database)** for ultra-fast storage.

---

## Semantic Search UI

![search_ui_meilisearch](./assets/search_ui_meilisearch.png)

- Support for vector search using `userProvided` embeddings
- Configurable hybrid search (`semanticRatio`, filters, sort)
- Search results with optional `_vectors` field for inspection

---

## Postman Collection

For quick testing of Meilisearch APIs (indexing, vector search, filtering):

[Postman Collection](./assets/Meilisearch.postman_collection.json)

---

## What Makes Meilisearch Unique?

- Built in **Rust** for performance and safety
- Typo tolerance out-of-the-box which they boasts about.
- Instant, prefix-aware search suggestions
- Semantic & hybrid search with user-defined embeddings as `source` embedders.

> © MIT Licensed. Meilisearch™ is a trademark of Meili SAS.
