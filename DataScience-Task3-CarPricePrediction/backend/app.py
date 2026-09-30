from flask import Flask, request, jsonify
import joblib
import os
import pandas as pd

app = Flask(__name__)

MODEL_PATH = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    "models",
    "car_price_model.pkl"
)

model = joblib.load(MODEL_PATH)


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
        data = request.get_json(silent=True)

        if not data:
            return jsonify({"error": "No JSON data received"}), 400

        # Accept both lowercase and frontend names
        km_driven = data.get("km_driven", data.get("Kms_Driven"))
        fuel = data.get("fuel", data.get("Fuel_Type"))
        seller_type = data.get(
            "seller_type",
            data.get("Seller_Type")
        )
        transmission = data.get(
            "transmission",
            data.get("Transmission")
        )
        owner = data.get("owner", data.get("Owner"))
        car_age = data.get("Car_Age", data.get("car_age"))
        brand = data.get("Brand", data.get("brand"))

        missing = []

        if km_driven is None:
            missing.append("km_driven")

        if fuel is None:
            missing.append("fuel")

        if seller_type is None:
            missing.append("seller_type")

        if transmission is None:
            missing.append("transmission")

        if owner is None:
            missing.append("owner")

        if car_age is None:
            missing.append("Car_Age")

        if brand is None:
            missing.append("Brand")

        if missing:
            return jsonify({
                "error": "Missing fields",
                "missing": missing
            }), 400

        # EXACT format expected by trained pipeline
        input_data = pd.DataFrame([{
            "km_driven": float(km_driven),
            "fuel": str(fuel),
            "seller_type": str(seller_type),
            "transmission": str(transmission),
            "owner": str(owner),
            "Car_Age": int(car_age),
            "Brand": str(brand)
        }])

        print("Input:")
        print(input_data)
        print(input_data.dtypes)

        prediction = model.predict(input_data)[0]

        return jsonify({
            "predicted_price": round(float(prediction), 2)
        })

    except Exception as e:
        print("Prediction error:", str(e))

        return jsonify({
            "error": str(e)
        }), 400


if __name__ == "__main__":
    app.run(debug=True)