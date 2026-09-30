import os
import joblib
import pandas as pd


# Get the Task 3 project directory
BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

# Path to Task 3 trained model
MODEL_PATH = os.path.join(
    BASE_DIR,
    "models",
    "car_price_model.pkl"
)


# Load trained model
model = joblib.load(MODEL_PATH)


def predict_car_price(car_data):
    """
    Predict the selling price of a used car.
    """

    input_data = pd.DataFrame([car_data])

    prediction = model.predict(input_data)

    return float(prediction[0])