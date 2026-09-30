import streamlit as st
import joblib
import os


# Load trained model
MODEL_PATH = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    "models",
    "spam_model.pkl"
)

model = joblib.load(MODEL_PATH)


# Page configuration
st.set_page_config(
    page_title="Email Spam Detector",
    page_icon="📧",
    layout="centered"
)


# Title
st.title("📧 Email Spam Detection")
st.write("Enter an email message to classify it as **Spam** or **Ham**.")


# Email input
message = st.text_area(
    "Enter Email Message",
    height=200,
    placeholder="Paste your email message here..."
)


# Prediction button
if st.button("Predict", type="primary"):

    if not message.strip():
        st.warning("Please enter an email message.")

    else:
        prediction = model.predict([message])[0]

        if prediction == 1:
            st.error("🚨 SPAM")
            st.write("This email is classified as **Spam**.")

        else:
            st.success("✅ HAM")
            st.write("This email is classified as **Ham (Not Spam)**.")