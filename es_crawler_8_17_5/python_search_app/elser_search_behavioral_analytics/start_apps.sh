#!/bin/bash

# Move to the script directory
cd "$(dirname "$0")"

# Create a logs directory if not exists
mkdir -p logs

# Start LLM term generator in background
echo "Starting llm_term_generator.py..."
nohup python3 ./llm_service/llm_term_generator.py > logs/llm_term_generator.log 2>&1 &

# Start image_plus_elser_app in background
echo "Starting image_plus_elser_app.with_analytics.py..."
nohup python3 image_plus_elser_app.with_analytics.py > logs/image_plus_elser_app.with_analytics.log 2>&1 &

# Optional: Show tail of logs
echo "Tailing both logs (Ctrl+C to exit)..."
tail -f logs/*.log
