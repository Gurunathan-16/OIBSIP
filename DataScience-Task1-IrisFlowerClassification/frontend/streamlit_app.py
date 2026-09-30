import streamlit as st
import requests
import pandas as pd


# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="Iris AI Classifier",
    page_icon="🌸",
    layout="wide"
)

API_URL = "http://127.0.0.1:5000"


# --------------------------------------------------
# API FUNCTIONS
# --------------------------------------------------

def get_prediction(data):
    """Send prediction request to Flask API."""
    try:
        response = requests.post(
            f"{API_URL}/predict",
            json=data,
            timeout=10
        )
        return response.json(), response.status_code

    except requests.exceptions.ConnectionError:
        return {
            "error": "Cannot connect to the Flask backend. Please start the backend server."
        }, 500

    except requests.exceptions.Timeout:
        return {
            "error": "The prediction request timed out. Please try again."
        }, 500

    except Exception as e:
        return {"error": str(e)}, 500


def get_history():
    """Get prediction history from Flask API."""
    try:
        response = requests.get(
            f"{API_URL}/history",
            timeout=10
        )
        return response.json(), response.status_code

    except requests.exceptions.ConnectionError:
        return {
            "error": "Cannot connect to the Flask backend. Please start the backend server."
        }, 500

    except requests.exceptions.Timeout:
        return {
            "error": "The history request timed out. Please try again."
        }, 500

    except Exception as e:
        return {"error": str(e)}, 500


# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.title("🌸 Iris AI Classifier")
st.caption("Predict Iris flower species using Machine Learning")

st.divider()


# --------------------------------------------------
# NAVIGATION
# --------------------------------------------------

page = st.sidebar.radio(
    "Navigation",
    ["🔮 Predict Flower", "📊 Prediction History", "ℹ️ About"]
)


# ==================================================
# PAGE 1 — PREDICTION
# ==================================================

if page == "🔮 Predict Flower":

    st.header("🔮 Predict Flower Species")

    st.write(
        "Enter the flower measurements in centimeters (cm) and let the "
        "machine learning model predict the Iris species."
    )

    # Create input columns
    col1, col2 = st.columns(2)

    with col1:
        sepal_length = st.number_input(
            "Sepal Length (cm)",
            min_value=0.0,
            max_value=10.0,
            value=5.1,
            step=0.1
        )

        sepal_width = st.number_input(
            "Sepal Width (cm)",
            min_value=0.0,
            max_value=10.0,
            value=3.5,
            step=0.1
        )

    with col2:
        petal_length = st.number_input(
            "Petal Length (cm)",
            min_value=0.0,
            max_value=10.0,
            value=1.4,
            step=0.1
        )

        petal_width = st.number_input(
            "Petal Width (cm)",
            min_value=0.0,
            max_value=10.0,
            value=0.2,
            step=0.1
        )

    st.write("")

    if st.button("🔮 Predict Species", use_container_width=True):

        input_data = {
            "sepal_length": sepal_length,
            "sepal_width": sepal_width,
            "petal_length": petal_length,
            "petal_width": petal_width
        }

        with st.spinner("🤖 Analyzing flower measurements..."):
            result, status = get_prediction(input_data)

        if status == 200 and result.get("success"):

            st.success("✅ Prediction completed successfully!")

            # Use native Streamlit components for guaranteed visibility
            st.subheader("🌸 Prediction Result")

            result_col1, result_col2 = st.columns(2)

            with result_col1:
                st.metric(
                    label="Predicted Species",
                    value=result.get("prediction", "Unknown")
                )

            with result_col2:
                confidence = result.get("confidence")

                if confidence is not None:
                    st.metric(
                        label="Model Confidence",
                        value=f"{confidence}%"
                    )
                else:
                    st.metric(
                        label="Model Confidence",
                        value="Not Available"
                    )

            st.info(
                f"🗄️ Prediction ID: #{result.get('prediction_id', 'N/A')} "
                "— This prediction has been saved to the SQLite database."
            )

        else:
            st.error(
                result.get(
                    "error",
                    "Something went wrong while making the prediction."
                )
            )


# ==================================================
# PAGE 2 — PREDICTION HISTORY
# ==================================================

elif page == "📊 Prediction History":

    st.header("📊 Prediction History")

    st.write(
        "All predictions made through the application are stored in the SQLite database."
    )

    # Refresh button
    if st.button("🔄 Refresh History"):
        st.rerun()

    # Automatically load history
    with st.spinner("Loading prediction history..."):
        result, status = get_history()

    if status == 200 and result.get("success"):

        predictions = result.get("predictions", [])

        if predictions:

            st.success(
                f"Found {result.get('count', len(predictions))} prediction(s)."
            )

            history_df = pd.DataFrame(predictions)

            # Select only available columns to prevent errors
            display_columns = [
                "id",
                "prediction",
                "confidence",
                "created_at",
                "sepal_length",
                "sepal_width",
                "petal_length",
                "petal_width"
            ]

            available_columns = [
                col for col in display_columns
                if col in history_df.columns
            ]

            history_df = history_df[available_columns]

            # Rename columns for better display
            column_names = {
                "id": "ID",
                "prediction": "Predicted Species",
                "confidence": "Confidence (%)",
                "created_at": "Created At",
                "sepal_length": "Sepal Length",
                "sepal_width": "Sepal Width",
                "petal_length": "Petal Length",
                "petal_width": "Petal Width"
            }

            history_df = history_df.rename(columns=column_names)

            # Display table
            st.dataframe(
                history_df,
                use_container_width=True,
                hide_index=True
            )

        else:
            st.info(
                "📭 No predictions found yet. Go to 'Predict Flower' and make your first prediction!"
            )

    else:
        st.error(
            result.get(
                "error",
                "Could not load prediction history."
            )
        )


# ==================================================
# PAGE 3 — ABOUT
# ==================================================

elif page == "ℹ️ About":

    st.header("ℹ️ About This Project")

    st.markdown("""
### 🌸 Iris Flower Classification

This full-stack machine learning application predicts the species of an
Iris flower based on four physical measurements.

### 📏 Input Features

- Sepal Length
- Sepal Width
- Petal Length
- Petal Width

### 🛠️ Technology Stack

| Component | Technology |
|-----------|------------|
| Frontend | Streamlit |
| Backend | Flask REST API |
| Machine Learning | Scikit-learn |
| Database | SQLite |

### 🔄 Application Flow

**User Input → Streamlit → Flask API → ML Model → SQLite → Result**
""")


# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.divider()
st.caption("🌸 Iris AI Classifier | Full-Stack Machine Learning Application")