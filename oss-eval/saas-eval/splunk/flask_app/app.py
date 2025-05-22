from flask import Flask
import logging
import time

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.route('/')
def hello():
    logger.info("Handling request to root endpoint")
    return "Hello, World!"

@app.route('/compute')
def compute():
    logger.info("Starting computation")
    time.sleep(1)  # Simulate computation
    logger.info("Computation finished")
    return "Computation done!"
