# 🚗 Car Price Prediction

## 📌 Project Overview

Car Price Prediction is a Machine Learning project developed as part of the **Oasis Infobyte Data Science Internship**.

The project predicts the **selling price of a used car** based on various factors such as the car's present price, age, kilometers driven, fuel type, seller type, transmission, and number of previous owners.

The project includes a complete Machine Learning workflow from data preprocessing and model training to prediction through a user-friendly Streamlit application and Flask API.

---

## 🎯 Objective

The main objective of this project is to develop a Machine Learning model that can estimate the selling price of a used car based on its characteristics.

### Key objectives

* Analyze the used-car dataset.
* Perform data preprocessing and feature engineering.
* Extract useful information such as car brand and car age.
* Train multiple regression models.
* Evaluate model performance using regression metrics.
* Save the trained model for future predictions.
* Build a simple interface for real-time car price prediction.

---

## 📊 Dataset

The project uses a used-car dataset containing information about cars and their selling prices.

### Dataset Features

| Feature         | Description               |
| --------------- | ------------------------- |
| `Car_Name`      | Name of the car           |
| `Year`          | Manufacturing year        |
| `Selling_Price` | Target selling price      |
| `Present_Price` | Current/ex-showroom price |
| `Kms_Driven`    | Kilometers driven         |
| `Fuel_Type`     | Type of fuel used         |
| `Seller_Type`   | Individual or dealer      |
| `Transmission`  | Manual or automatic       |
| `Owner`         | Number of previous owners |

### Feature Engineering

Two additional features are created during preprocessing:

* **Car_Age** = Current Year − Manufacturing Year
* **Brand** = First word extracted from `Car_Name`

These features help the model use more meaningful information about the vehicle.

---

## 🔄 Machine Learning Workflow

The project follows these steps:

```text
Dataset
   ↓
Data Exploration
   ↓
Data Cleaning
   ↓
Feature Engineering
   ↓
Categorical Feature Encoding
   ↓
Train-Test Split
   ↓
Model Training
   ↓
Model Evaluation
   ↓
Best Model Selection
   ↓
Model Saving
   ↓
Prediction Application
```

---

## 🤖 Machine Learning Models

Two regression algorithms were implemented and compared:

### 1. Linear Regression

Linear Regression is used as a baseline regression model to understand the relationship between the input features and the car's selling price.

### 2. Random Forest Regressor

Random Forest Regressor combines multiple decision trees to improve prediction performance and handle nonlinear relationships between features.

The models are evaluated and the better-performing model is saved as:

```text
models/car_price_model.pkl
```

---

## 📏 Evaluation Metrics

The following metrics are used to evaluate the regression models:

### Mean Absolute Error (MAE)

Measures the average absolute difference between the actual and predicted prices.

### Root Mean Squared Error (RMSE)

Measures the square root of the average squared prediction error.

### R² Score

Measures how well the model explains the variation in the target variable.

Higher R² and lower MAE/RMSE indicate better model performance.

---

## 🖥️ Application

The project provides a **Streamlit web application** where users can enter car details and receive a predicted selling price.

### Input Parameters

* Car Brand
* Present Price
* Kilometers Driven
* Car Age
* Fuel Type
* Seller Type
* Transmission
* Number of Previous Owners

The application sends these details to the trained Machine Learning model and displays the estimated selling price.

---

## 🔌 Flask API

A Flask backend is also included for serving predictions through an API.

### Available Endpoints

| Endpoint   | Method | Description               |
| ---------- | ------ | ------------------------- |
| `/`        | GET    | API information           |
| `/health`  | GET    | Check API status          |
| `/predict` | POST   | Predict car selling price |
| `/history` | GET    | View prediction history   |

The API allows the trained model to be integrated with other applications.

---

## 📁 Project Structure

```text
DataScience-Task3-CarPricePrediction/
│
├── data/
│   ├── car_data.csv
│   └── predictions.db
│
├── notebooks/
│   └── Car_Price_Prediction.ipynb
│
├── models/
│   └── car_price_model.pkl
│
├── backend/
│   ├── app.py
│   ├── model.py
│   └── database.py
│
├── frontend/
│   └── streamlit_app.py
│
├── screenshots/
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🛠️ Technologies Used

* **Python**
* **Pandas**
* **NumPy**
* **Scikit-learn**
* **Matplotlib**
* **Seaborn**
* **Joblib**
* **Flask**
* **Streamlit**
* **SQLite**

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/Gurunathan-16/OIBSIP.git
```

Navigate to the Task 3 directory:

```bash
cd OIBSIP/DataScience-Task3-CarPricePrediction
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Streamlit Application

From the Task 3 directory, run:

```bash
python -m streamlit run frontend/streamlit_app.py
```

The Streamlit application will open in your browser.

Enter the required car details and click the prediction button to receive the estimated selling price.

---

## ▶️ Run the Flask API

From the Task 3 directory:

```bash
python backend/app.py
```

The Flask API will start locally.

You can check the API health using:

```text
/health
```

and send prediction requests through:

```text
/predict
```

---

## 🧪 Example Prediction

Example input:

```text
Brand: Honda
Present Price: 5.59
Kms Driven: 27000
Car Age: 11
Fuel Type: Petrol
Seller Type: Dealer
Transmission: Manual
Owner: 0
```

The application processes these inputs and returns the predicted selling price generated by the trained Machine Learning model.

---

## 💡 Key Learning Outcomes

Through this project, I gained practical experience in:

* Data preprocessing
* Exploratory Data Analysis
* Feature engineering
* Categorical data handling
* Regression algorithms
* Model comparison
* Model evaluation
* Model serialization using Joblib
* Building Flask APIs
* Building Streamlit applications
* Integrating Machine Learning models into applications

---

## 🚀 Future Improvements

Possible improvements include:

* Using larger and more diverse car datasets.
* Hyperparameter tuning.
* Testing additional regression algorithms.
* Improving model accuracy.
* Deploying the application online.
* Adding visual analytics to the prediction interface.

---

## 👨‍💻 Author

**Gurunathan R**

M.Sc. Computer Science
Bishop Heber College, Trichy

GitHub: `https://github.com/Gurunathan-16`

---

## 📌 Internship

This project was completed as part of the:

**Oasis Infobyte Data Science Internship**

### Task 3 — Car Price Prediction

#OasisInfobyte #DataScience #MachineLearning #Python #CarPricePrediction #Internship
