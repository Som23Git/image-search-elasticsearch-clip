# llm_term_generator.py

from flask import Flask, jsonify
from transformers import pipeline
from flask_cors import CORS
import random
from elasticapm.contrib.flask import ElasticAPM
import config

app = Flask(__name__)
CORS(app)

port = config.EXPOSE_PORT

app.config['ELASTIC_APM'] = {
    'SERVICE_NAME': config.APM_SERVICE_NAME,
    'SERVER_URL': config.APM_SERVER_URL,
    'SECRET_TOKEN': config.APM_SECRET_TOKEN,
    'ENVIRONMENT': config.APM_APP_ENVIRONMENT
}

apm = ElasticAPM(app)

# Predefined good terms
hardcoded_terms = [
    "Recipe for pasta",
    "How to make pizza",
    "Quick meal sandwich",
    "Ingredients for salad",
    "Cook spicy noodles",
    "Easy recipe pancakes",
    "Best dish butter chicken",
    "Food with avocado toast"
]

def generate_fake_terms():
    return [random.choice(hardcoded_terms)]

# Load a very lightweight text generation model
# generator = pipeline("text-generation", model="distilgpt2")

# # Pre-defined prompt templates for recipe context
# prompts = [
#     "Recipe for", "How to make", "Ingredients for", "Easy recipe", "Quick meal", "Best dish", "Cook", "Food with"
# ]

# def generate_fake_terms():
#     prompts = [
#         "Recipe for", "How to make", "Ingredients for",
#         "Easy recipe", "Quick meal", "Best dish",
#         "Cook", "Food with"
#     ]
#     prompt = random.choice(prompts)

#     output = generator(
#         prompt,
#         max_new_tokens=10,    # Only small extension
#         num_return_sequences=1,
#         do_sample=True,
#         temperature=0.8,
#         top_p=0.9
#     )

#     generated_text = output[0]['generated_text']

#     # Remove the prompt from beginning to get only new text
#     new_part = generated_text.replace(prompt, '').strip()

#     # Combine cleanly
#     search_phrase = (prompt + " " + new_part).strip()

#     return [search_phrase]

@app.route('/random-terms', methods=['GET'])
def random_terms():
    terms = generate_fake_terms()
    return jsonify(terms)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=port)