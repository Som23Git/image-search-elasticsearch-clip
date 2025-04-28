# Elasticsearch Recipe Search Projects

This repository contains various projects and experiments for **search applications** built on **Elasticsearch**, using **Python-based** implementations and some testing files.

## Projects Overview

- **`python_search_app/`**: Python-based search applications, including:
  - **`elser_search/`**: Text-based recipe search using Elasticsearch ELSER.
  - **`image_search/`**: Search recipes by image using CLIP embeddings and Elasticsearch kNN.
  - **`image_plus_elser_search/`**: Combines both text (ELSER) and image (CLIP) search with APM & RUM instrumentation and Bootstrap UI.
  - **`generate_embeddings_app/`**: Standalone app to generate and view CLIP image embeddings.

## How to Navigate

For the **Python Search Applications**, see:

- [`python_search_app/`](./python_search_app)

Each subdirectory includes its own `README.md` with setup and usage instructions.

## License

This project is licensed under the [MIT License](./LICENSE).