from flask import Flask, request, jsonify
from flask_cors import CORS

from model import predict_species
from database import (
    initialize_database,
    save_prediction,
    get_prediction_history
)


app = Flask(__name__)
CORS(app)


# Initialize database when the application starts
initialize_database()


@app.route("/", methods=["GET"])
def home():
    """Welcome endpoint."""
    return jsonify({
        "message": "Iris Flower Classification API is running!"
    })


@app.route("/health", methods=["GET"])
def health():
    """Check API health."""
    return jsonify({
        "status": "healthy",
        "service": "Iris Flower Classification API"
    })


@app.route("/predict", methods=["POST"])
def predict():
    """Predict Iris flower species and save the result."""

    try:
        data = request.get_json()

        if not data:
            return jsonify({
                "error": "No input data provided"
            }), 400

        required_fields = [
            "sepal_length",
            "sepal_width",
            "petal_length",
            "petal_width"
        ]

        missing_fields = [
            field for field in required_fields
            if field not in data
        ]

        if missing_fields:
            return jsonify({
                "error": "Missing required fields",
                "missing_fields": missing_fields
            }), 400

        # Convert input values to float
        sepal_length = float(data["sepal_length"])
        sepal_width = float(data["sepal_width"])
        petal_length = float(data["petal_length"])
        petal_width = float(data["petal_width"])

        # Get ML prediction
        result = predict_species(
            sepal_length,
            sepal_width,
            petal_length,
            petal_width
        )

        # Save prediction to SQLite database
        prediction_id = save_prediction(
            sepal_length=sepal_length,
            sepal_width=sepal_width,
            petal_length=petal_length,
            petal_width=petal_width,
            prediction=result["prediction"],
            confidence=result.get("confidence")
        )

        # Return response
        return jsonify({
            "success": True,
            "prediction_id": prediction_id,
            "input": {
                "sepal_length": sepal_length,
                "sepal_width": sepal_width,
                "petal_length": petal_length,
                "petal_width": petal_width
            },
            **result
        })

    except ValueError:
        return jsonify({
            "error": "All measurements must be valid numbers"
        }), 400

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500


@app.route("/history", methods=["GET"])
def history():
    """Get all previous predictions."""

    try:
        predictions = get_prediction_history()

        return jsonify({
            "success": True,
            "count": len(predictions),
            "predictions": predictions
        })

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500


if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )