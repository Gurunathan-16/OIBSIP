import os
import joblib
import numpy as np


# Get the absolute path of the project directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Path to the trained ML model
MODEL_PATH = os.path.join(BASE_DIR, "models", "iris_model.pkl")


# Load the trained model
model = joblib.load(MODEL_PATH)


# Iris class names
SPECIES = ["Setosa", "Versicolor", "Virginica"]


def predict_species(sepal_length, sepal_width, petal_length, petal_width):
    """
    Predict the Iris flower species using the trained ML model.
    """

    # Create input array in the same order used during training
    features = np.array([
        [sepal_length, sepal_width, petal_length, petal_width]
    ])

    # Make prediction
    prediction = model.predict(features)[0]

    # Get prediction probability if supported by the model
    probabilities = None

    if hasattr(model, "predict_proba"):
        probabilities = model.predict_proba(features)[0]

    result = {
        "prediction": SPECIES[int(prediction)]
    }

    # Add confidence scores if available
    if probabilities is not None:
        result["confidence"] = round(
            float(max(probabilities)) * 100,
            2
        )

    return result