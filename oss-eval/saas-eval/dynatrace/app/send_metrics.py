import os
import requests
import time

def send_custom_metric(metric_name, value):
    dynatrace_url = os.getenv("DT_ENV_URL")
    token = os.getenv("DT_API_TOKEN")
    ingest_url = f"{dynatrace_url}/api/v2/metrics/ingest"

    payload = f"{metric_name},source=docker_app gauge,{value} {int(time.time() * 1000)}"

    headers = {
        "Authorization": f"Api-Token {token}",
        "Content-Type": "text/plain; charset=utf-8"
    }

    response = requests.post(ingest_url, headers=headers, data=payload)
    print(f"[Dynatrace] Status: {response.status_code}, Response: {response.text}")

    # ⬇️ Log the metric send attempt to persistent volume
    try:
        os.makedirs("/app/data", exist_ok=True)  # Ensure dir exists
        with open("/app/data/metrics.log", "a") as f:
            f.write(f"{time.ctime()}: Sent {metric_name} = {value} (status: {response.status_code})\n")
    except Exception as e:
        print(f"[ERROR] Failed to log metric: {e}")
