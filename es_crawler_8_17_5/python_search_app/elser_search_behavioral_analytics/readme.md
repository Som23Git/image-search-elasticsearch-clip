# Behavioral Analytics Recipe Search App

This project demonstrates a full-stack example of tracking **user behavior** on a **Flask + Elasticsearch** recipe search application.  
It integrates **Elastic RUM (Real User Monitoring)** and **Elastic Behavioral Analytics** to capture search and click events automatically.

---

## Features

- Search recipes using text (Elser Search).
- Search recipes using image embeddings (Image Search).
- Track user search queries, click events, and behavior.
- Background simulation of random user searches and clicks.
- Real User Monitoring (APM) integration.
- Behavioral Analytics Tracker setup.
- Optional: Fake LLM generator for random search terms.

---

## Directory Structure

```
elser_search_behavioral_analytics
├── config.py
├── image_plus_elser_app.with_analytics.py
├── llm_service/
│   └── llm_term_generator.py
├── requirements.txt
├── static/
│   ├── js/
│   └── styles.css
├── templates/
    └── image_plus_elser_app_v1/

```

---

## Setup Instructions

1. Clone the repository.

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Set up your `config.py` with:
   - Elasticsearch URL
   - API Key
   - APM and RUM details
   - Behavioral Analytics API Key
   - Search Application name
   - Index and Template names

4. (Optional) Start the Fake Term Generator:

```bash
python3 llm_term_generator.py

# run in background
python3 llm_service/llm_term_generator.py > /dev/null 2>&1 &
```
Exposes the service in `http://127.0.0.1:5050/random-terms` to pass it in the `simulate.js`.

5. Run the main app:

```bash
python3 image_plus_elser_app.with_analytics.py
```

6. Visit `http://127.0.0.1:5000` to access the app.

---

## Simulating User Behavior

- Open browser console.
- Run:

```javascript
startSimulationManually()
```

This triggers random searches, clicks, and page reloads automatically for Behavioral Analytics testing.

---

## Requirements

- Flask
- elasticsearch
- transformers
- torch
- Pillow
- elastic-apm
- flask-cors (for LLM term generator)

Install with:

```bash
pip install flask elasticsearch transformers torch Pillow elastic-apm flask-cors
```

---

## About `llm_service/llm_term_generator.py`

- `llm_term_generator.py` is a **small Flask microservice**.
- It uses **HuggingFace's `distilgpt2` model** to generate **short random search terms**.
- These search terms mimic realistic user queries like:  
  _"Recipe for pasta"_, _"How to make pancakes"_, etc.
- The Flask app exposes an API endpoint `/random-terms` that returns one random generated term at a time.
- The simulated user script (`simulate_user.js`) **fetches these terms dynamically** to make the user behavior look more organic and realistic.

## Notes

- This project is for **testing and demo purposes**.
- For production, it is recommended to use a WSGI server like Gunicorn.
- Behavioral Analytics needs CORS to be enabled properly in Elasticsearch Cloud.

---

## License

This project is licensed under the **MIT License**.