# Elasticsearch Recipe Search Projects

This repository contains various projects and experiments for **search applications** built on **Elasticsearch**, using **Python-based** implementations and some testing files.

## Projects Overview

- **`python_search_app/`**: Python-based search applications, including:
  - **`elser_search/`**: Text-based recipe search using Elasticsearch ELSER.
  - **`image_search/`**: Search recipes by image using CLIP embeddings and Elasticsearch kNN.
  - **`image_plus_elser_search/`**: Combines both text (ELSER) and image (CLIP) search with APM & RUM instrumentation and Bootstrap UI.
  - **`generate_embeddings_app/`**: Standalone app to generate and view CLIP image embeddings.
  - **`elser_search_behavioral_analytics/`**:  Combines both text (ELSER) and image search with APM & RUM instrumentation and included Behavioral Analytics(for testing, it exposes a `llm_term_generator.py`)

## How to Navigate

For the **Python Search Applications**, see:

- [`python_search_app/`](./es_crawler_8_17_5/python_search_app/)

Each subdirectory includes its own `README.md` with setup and usage instructions.

## License

This project is licensed under the [MIT License](./LICENSE).

### ⚠️ Elasticsearch Licensing Notice

This project uses [Elasticsearch](https://www.elastic.co/elasticsearch/) for backend search functionality. Elasticsearch is licensed under the [Elastic License v2](https://www.elastic.co/licensing/elastic-license), which allows usage but restricts offering it as a managed service.

> **Note:** This project does not modify or redistribute Elasticsearch itself — it references the official Docker images.

The source code of this search application is MIT-licensed, and you are free to use, modify, and share it — but you are responsible for complying with the Elasticsearch license when deploying it.