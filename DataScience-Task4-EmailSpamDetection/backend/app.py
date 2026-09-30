from flask import Flask, request, jsonify
from flask_cors import CORS

from model import predict_spam
from database import create_table, save_prediction, get_predictions


app = Flask(__name__)
CORS(app)

create_table()


@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "Email Spam Detection API is running",
        "status": "success"
    })


@app.route("/health", methods=["GET"])
def health():
    return jsonify({
        "status": "healthy"
    })


@app.route("/predict", methods=["POST"])
def predict():

    data = request.get_json()

    if not data or "message" not in data:
        return jsonify({
            "error": "Message is required"
        }), 400

    message = data["message"]

    if not isinstance(message, str) or not message.strip():
        return jsonify({
            "error": "Message must be a non-empty string"
        }), 400

    prediction = predict_spam(message)

    save_prediction(
        message,
        prediction
    )

    return jsonify({
        "message": message,
        "prediction": prediction
    })


@app.route("/history", methods=["GET"])
def history():

    rows = get_predictions()

    predictions = []

    for row in rows:
        predictions.append({
            "id": row[0],
            "message": row[1],
            "prediction": row[2],
            "created_at": row[3]
        })

    return jsonify(predictions)


if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )