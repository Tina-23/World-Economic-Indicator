# app/main.py
from flask import Flask, request, jsonify
import os
import pickle
import pandas as pd

MODEL_PATH = os.environ.get("MODEL_PATH", "/app/models/model.pkl")

def load_model(path=MODEL_PATH):
    if not os.path.exists(path):
        raise FileNotFoundError(f"Model not found at {path}")
    with open(path, "rb") as f:
        model = pickle.load(f)
    return model

app = Flask(__name__)

# Lazy load model on first request or at startup
model = None
@app.before_first_request
def _load():
    global model
    try:
        model = load_model()
    except Exception as e:
        # Keep model = None and let /predict return error
        app.logger.error("Model load error: %s", e)
        model = None

@app.route("/", methods=["GET"])
def root():
    return jsonify({"status": "ok", "message": "POST /predict with JSON {'data': {...}} or {'data_list': [...]}"})

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok", "model_loaded": model is not None})

@app.route("/predict", methods=["POST"])
def predict():
    global model
    if model is None:
        return jsonify({"error": "model not loaded on server"}), 500

    payload = request.get_json()
    if payload is None:
        return jsonify({"error": "Expecting JSON payload"}), 400

    # support dict-of-features
    if "data" in payload and isinstance(payload["data"], dict):
        X = pd.DataFrame([payload["data"]])
    elif "data_list" in payload and isinstance(payload["data_list"], list):
        # if user provides list, convert to DataFrame with a numeric column order.
        # This requires the client to know feature ordering — not recommended.
        X = pd.DataFrame([payload["data_list"]])
    else:
        return jsonify({"error": "Provide 'data': {..} or 'data_list': [...]"}), 400

    try:
        preds = model.predict(X)
        # return list of predictions
        return jsonify({"predictions": [float(x) for x in preds]})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))
# app/main.py
