from flask import Flask, Response
import os
import time
import random
import requests
from datetime import datetime

app = Flask(__name__)

# Dynatrace config
DT_ENV_URL = os.getenv("DT_ENV_URL")
DT_API_TOKEN = os.getenv("DT_API_TOKEN")
HOST_ID = os.getenv("DT_HOST_ID", "manual-simulated-host")
METRIC_INGEST_URL = f"{DT_ENV_URL}/api/v2/metrics/ingest"
METRIC_HEADERS = {
    "Authorization": f"Api-Token {DT_API_TOKEN}",
    "Content-Type": "text/plain; charset=utf-8"
}
LOG_FILE = "/app/data/metrics.log"

# Reusable metric sender
def send_metric(metric_name, value, dimensions=""):
    timestamp = int(time.time() * 1000)
    line = f"{metric_name}{dimensions} gauge,{value} {timestamp}"
    resp = requests.post(METRIC_INGEST_URL, headers=METRIC_HEADERS, data=line)
    log(f"Sent metric: {line} (status: {resp.status_code})")
    return resp.status_code

# Local log writer
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

# Routes
@app.route('/')
def index():
    return 'Dynatrace Demo App is Running! Use /simulate or /random-temp'

@app.route('/simulate')
def simulate():
    import random
    value = random.randint(0, 2000)
    send_metric("demo.manual.metric", value)
    return f'Manual metric sent with value {value}!'

@app.route('/random-temp')
def random_temp():
    value = round(random.uniform(40.0, 80.0), 2)
    send_metric("simulated.cpu.temperature", value)
    return f'Random temperature metric sent: {value}°C'

@app.route('/logs')
def show_logs():
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as f:
            return Response(f.read(), mimetype='text/plain')
    else:
        return Response("No logs found.", status=404)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)