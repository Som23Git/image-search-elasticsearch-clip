#!/bin/bash

# Move to the script directory
cd "$(dirname "$0")"

# Stop llm_term_generator.py
echo "Stopping llm_term_generator.py..."
pkill -f llm_term_generator.py

# Stop image_plus_elser_app.with_analytics.py
echo "Stopping image_plus_elser_app.with_analytics.py..."
pkill -f image_plus_elser_app.with_analytics.py

echo "All background apps stopped."