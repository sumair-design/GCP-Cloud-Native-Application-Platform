import os
import time
from flask import Flask, Response, request
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

REQUEST_COUNT = Counter("cloud_native_http_requests_total","Total HTTP requests",["method","path","status"])
REQUEST_LATENCY = Histogram("cloud_native_http_request_duration_seconds","HTTP request latency",["method","path"])

@app.before_request
def start_timer():
    request._start_time = time.perf_counter()

@app.after_request
def record_metrics(response):
    elapsed = time.perf_counter() - getattr(request, "_start_time", time.perf_counter())
    REQUEST_COUNT.labels(request.method, request.path, response.status_code).inc()
    REQUEST_LATENCY.labels(request.method, request.path).observe(elapsed)
    return response

@app.get("/")
def index():
    return {
        "application": "GCP Cloud-Native Application Platform",
        "message": os.getenv("APP_MESSAGE", "Running on Google Kubernetes Engine"),
        "environment": os.getenv("APP_ENV", "development"),
        "pod": os.getenv("HOSTNAME", "unknown"),
        "version": os.getenv("APP_VERSION", "local")
    }

@app.get("/healthz")
def healthz():
    return {"status":"healthy"}

@app.get("/readyz")
def readyz():
    return {"status":"ready"}

@app.get("/metrics")
def metrics():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)
