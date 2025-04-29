# llm_term_generator.py

from flask import Flask, jsonify
from transformers import pipeline
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

# Load a very lightweight text generation model
generator = pipeline("text-generation", model="distilgpt2")

# Pre-defined prompt templates for recipe context
prompts = [
    "Recipe for", "How to make", "Ingredients for", "Easy recipe", "Quick meal", "Best dish", "Cook", "Food with"
]

def generate_fake_terms(num_terms=1):
    fake_terms = []
    for _ in range(num_terms):
        prompt = random.choice(prompts)
        output = generator(prompt, max_length=10, num_return_sequences=1)[0]['generated_text']
        # Post-process: only keep last few words to make it look like a search query
        clean_term = output.replace(prompt, "").strip().split("\n")[0]
        if clean_term:
            fake_terms.append((prompt + " " + clean_term).strip())
    return fake_terms

@app.route('/random-terms', methods=['GET'])
def random_terms():
    terms = generate_fake_terms()
    return jsonify(terms)

if __name__ == '__main__':
    app.run(port=5050)