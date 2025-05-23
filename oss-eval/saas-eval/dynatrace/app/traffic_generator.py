import os
import time
import random
import requests
import json
from datetime import datetime

# Config from environment variables
DT_ENV_URL = os.getenv("DT_ENV_URL")
DT_API_TOKEN = os.getenv("DT_API_TOKEN")
HOST_ID = os.getenv("DT_HOST_ID", "manual-simulated-host")

# Endpoints
METRIC_INGEST_URL = f"{DT_ENV_URL}/api/v2/metrics/ingest"
LOG_INGEST_URL = f"{DT_ENV_URL}/api/v2/logs/ingest"

# Headers
METRIC_HEADERS = {
    "Authorization": f"Api-Token {DT_API_TOKEN}",
    "Content-Type": "text/plain; charset=utf-8"
}
LOG_HEADERS = {
    "Authorization": f"Api-Token {DT_API_TOKEN}",
    "Content-Type": "application/json; charset=utf-8"
}

# Metric name
METRIC_NAME = "simulated.cpu.temperature"

# Log file
LOG_FILE = "/app/data/metrics.log"

def send_metric(value):
    timestamp = int(time.time() * 1000)
    line = f"{METRIC_NAME},dt.entity.host={HOST_ID},core=1 gauge,{value} {timestamp}"
    resp = requests.post(METRIC_INGEST_URL, headers=METRIC_HEADERS, data=line)
    log(f"Sent metric: {line} (status: {resp.status_code})")

def send_log(message, level="info"):
    log_data = [{
        "content": message,
        "status": level,
        "service.name": "simulator",
        "service.namespace": "demo",
        "custom.source": "python_script"
    }]
    resp = requests.post(LOG_INGEST_URL, headers=LOG_HEADERS, data=json.dumps(log_data))
    log(f"Sent log: {message} (status: {resp.status_code})")

def log(msg):
    timestamp = datetime.utcnow().isoformat()
    full_msg = f"{timestamp} | {msg}"
    print(full_msg)
    try:
        os.makedirs("/app/data", exist_ok=True)
        with open(LOG_FILE, "a") as f:
            f.write(full_msg + "\n")
    except Exception as e:
        print(f"[ERROR writing to log] {e}")

def simulate_traffic():
    print("Starting traffic generator loop...")
    while True:
        value = round(random.uniform(40.0, 80.0), 2)  # Simulated temperature
        send_metric(value)
        send_log(f"CPU temp simulated at {value}°C")
        time.sleep(5)  # Sleep for 5 seconds

if __name__ == "__main__":
    log("Starting traffic generator...")
    simulate_traffic()
