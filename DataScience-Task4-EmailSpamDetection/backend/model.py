import os
import joblib

MODEL_PATH = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    "models",
    "spam_model.pkl"
)

model = joblib.load(MODEL_PATH)


def predict_spam(message):
    prediction = model.predict([message])[0]

    if prediction == 1:
        return "SPAM"
    else:
        return "HAM"