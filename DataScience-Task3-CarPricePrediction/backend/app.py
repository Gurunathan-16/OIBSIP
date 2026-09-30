from flask import Flask, request, jsonify
from flask_cors import CORS

from model import predict_car_price

from database import (
    create_table,
    save_prediction,
    get_predictions
)


app = Flask(__name__)

CORS(app)


# Create database table when application starts
create_table()


@app.route("/", methods=["GET"])
def home():

    return jsonify({
        "message": "Car Price Prediction API is running"
    })


@app.route("/health", methods=["GET"])
def health():

    return jsonify({
        "status": "healthy"
    })


@app.route("/predict", methods=["POST"])
def predict():

    try:

        data = request.get_json()

        required_fields = [
            "Present_Price",
            "Kms_Driven",
            "Fuel_Type",
            "Seller_Type",
            "Transmission",
            "Owner",
            "Car_Age",
            "Brand"
        ]

        # Check missing fields
        missing_fields = [
            field
            for field in required_fields
            if field not in data
        ]

        if missing_fields:

            return jsonify({
                "success": False,
                "error": "Missing required fields",
                "missing_fields": missing_fields
            }), 400

        # Prepare input data
        car_data = {
            "Present_Price": float(data["Present_Price"]),
            "Kms_Driven": float(data["Kms_Driven"]),
            "Fuel_Type": str(data["Fuel_Type"]).strip(),
            "Seller_Type": str(data["Seller_Type"]).strip(),
            "Transmission": str(data["Transmission"]).strip(),
            "Owner": int(data["Owner"]),
            "Car_Age": int(data["Car_Age"]),
            "Brand": str(data["Brand"]).strip()
        }

        # Predict price
        predicted_price = predict_car_price(car_data)

        # Save prediction
        save_prediction(
            present_price=car_data["Present_Price"],
            kms_driven=car_data["Kms_Driven"],
            fuel_type=car_data["Fuel_Type"],
            seller_type=car_data["Seller_Type"],
            transmission=car_data["Transmission"],
            owner=car_data["Owner"],
            car_age=car_data["Car_Age"],
            brand=car_data["Brand"],
            predicted_price=predicted_price
        )

        return jsonify({
            "success": True,
            "predicted_price": round(predicted_price, 2),
            "message": "Prediction saved successfully"
        })

    except ValueError:

        return jsonify({
            "success": False,
            "error": "Please provide valid numeric values."
        }), 400

    except Exception as e:

        return jsonify({
            "success": False,
            "error": str(e)
        }), 500


@app.route("/history", methods=["GET"])
def history():

    try:

        predictions = get_predictions()

        return jsonify({
            "success": True,
            "count": len(predictions),
            "predictions": predictions
        })

    except Exception as e:

        return jsonify({
            "success": False,
            "error": str(e)
        }), 500


if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )