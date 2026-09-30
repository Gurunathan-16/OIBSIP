# Iris Flower Classification

## Project Overview

This project uses Machine Learning to classify Iris flowers into three species based on their sepal and petal measurements.

The project was developed as part of the **Oasis Infobyte Data Science Internship**.

## Objective

The objective is to build a classification model that predicts the species of an Iris flower from its:

* Sepal Length
* Sepal Width
* Petal Length
* Petal Width

The three classes are:

* Iris Setosa
* Iris Versicolor
* Iris Virginica

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Seaborn
* Joblib
* Flask
* Streamlit
* Jupyter Notebook

## Dataset

The project uses the **Iris dataset**, which contains measurements of Iris flowers along with their corresponding species.

### Features

| Feature      | Description         |
| ------------ | ------------------- |
| Sepal Length | Length of the sepal |
| Sepal Width  | Width of the sepal  |
| Petal Length | Length of the petal |
| Petal Width  | Width of the petal  |

### Target

The target variable is the Iris species:

* Setosa
* Versicolor
* Virginica

## Machine Learning Workflow

1. Load the Iris dataset
2. Explore the dataset
3. Check data structure and statistics
4. Visualize feature relationships
5. Prepare features and target
6. Split the data into training and testing sets
7. Train the classification model
8. Evaluate model performance
9. Save the trained model
10. Use the model for new predictions

## Project Structure

```text
DataScience-L1-IrisFlowerClassification/
│
├── data/
│
├── notebooks/
│   └── Iris_Flower_Classification.ipynb
│
├── models/
│   └── iris_model.pkl
│
├── backend/
│
├── frontend/
│
├── requirements.txt
├── .gitignore
└── README.md
```

## Model

A machine learning classification model is trained using the Iris dataset and saved as:

```text
models/iris_model.pkl
```

The saved model is used by the application to make predictions for new flower measurements.

## Application

The project includes a prediction interface where users can provide:

* Sepal Length
* Sepal Width
* Petal Length
* Petal Width

The application then predicts the corresponding Iris species.

## How to Run

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Run the application

If the project uses Streamlit:

```bash
streamlit run frontend/streamlit_app.py
```

If the project uses Flask:

```bash
python backend/app.py
```

Use the command corresponding to the application included in the project.

## Example Prediction

Example input:

```text
Sepal Length: 5.1
Sepal Width: 3.5
Petal Length: 1.4
Petal Width: 0.2
```

The model predicts:

```text
Iris Setosa
```

## Conclusion

This project demonstrates the use of Machine Learning for multi-class classification and provides an application interface for predicting Iris flower species from flower measurements.
