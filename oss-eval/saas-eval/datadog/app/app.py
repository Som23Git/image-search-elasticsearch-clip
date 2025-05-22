from flask import Flask, jsonify
import psycopg2

# Datadog APM auto-instrumentation
from ddtrace import patch_all, tracer
patch_all()

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "Welcome to the Datadog APM demo!"})

@app.route("/db")
def db_query():
    try:
        conn = psycopg2.connect(
            host="db", dbname="sampledb", user="postgres", password="postgres"
        )
        cur = conn.cursor()
        cur.execute("SELECT NOW();")
        row = cur.fetchone()
        conn.close()
        return jsonify({"db_time": str(row[0])})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
