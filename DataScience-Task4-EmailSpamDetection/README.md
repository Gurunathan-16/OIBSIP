# 📧 Email Spam Detection

## 📌 Project Overview

Email Spam Detection is a Machine Learning project developed as part of the **Oasis Infobyte Data Science Internship**.

The project uses Natural Language Processing (NLP) and Machine Learning techniques to classify email messages as either **Spam** or **Ham (Not Spam)**.

The system preprocesses email text, converts the text into numerical features using **TF-IDF**, trains multiple classification models, compares their performance, and uses the best-performing model for real-time predictions through a Streamlit application.

---

## 🎯 Objective

The main objective of this project is to build a Machine Learning model that can automatically identify unwanted or spam emails from normal emails.

### Key objectives

* Analyze and preprocess email text.
* Clean unnecessary characters, URLs, and email addresses.
* Convert text into numerical features using TF-IDF.
* Train multiple Machine Learning classification models.
* Compare model performance using classification metrics.
* Select the best-performing model.
* Save the trained model for future predictions.
* Build a simple web application for real-time spam detection.

---

## 📊 Dataset

The project uses an email spam dataset containing email messages and their corresponding labels.

### Dataset Information

| Column | Description                                       |
| ------ | ------------------------------------------------- |
| `text` | Full email message                                |
| `spam` | Target label indicating whether the email is spam |

### Target Values

```text
0 → Ham (Not Spam)
1 → Spam
```

The dataset contains **5,728 email messages**.

---

## 🧹 Text Preprocessing

Email messages are cleaned before being provided to the Machine Learning models.

The preprocessing includes:

* Converting text to lowercase.
* Removing URLs.
* Removing email addresses.
* Removing unnecessary special characters.
* Removing extra spaces.
* Preparing clean text for feature extraction.

Example:

```text
Original:
Congratulations! You won $1000. Visit http://example.com

After preprocessing:
congratulations you won visit
```

---

## 🔢 Feature Extraction

### TF-IDF

**Term Frequency-Inverse Document Frequency (TF-IDF)** is used to convert email text into numerical feature vectors.

The project uses:

```text
ngram_range = (1, 2)
stop_words = "english"
max_features = 10000
```

This allows the model to learn from both individual words and two-word combinations.

---

## 🤖 Machine Learning Models

Three classification algorithms were trained and compared.

### 1. Logistic Regression

Logistic Regression is used as a baseline classification model for identifying spam and ham emails.

### 2. Multinomial Naive Bayes

Multinomial Naive Bayes is commonly used for text classification problems and works effectively with TF-IDF features.

### 3. Linear Support Vector Machine

Linear SVM is used to find an effective decision boundary between spam and ham messages.

---

## 📈 Model Performance

The trained models were evaluated using Accuracy, Precision, Recall, and F1 Score.

| Model                   |   Accuracy | Precision |     Recall |   F1 Score |
| ----------------------- | ---------: | --------: | ---------: | ---------: |
| Logistic Regression     |     98.42% |    99.23% |     94.16% |     96.63% |
| Multinomial Naive Bayes |     98.51% |    99.61% |     94.16% |     96.81% |
| Linear SVM              | **99.30%** |    98.90% | **98.18%** | **98.53%** |

Based on the evaluation results, **Linear SVM achieved the highest F1 Score and accuracy among the tested models**.

The trained model is saved as:

```text
models/spam_model.pkl
```

---

## 🔄 Machine Learning Workflow

```text
Email Dataset
      ↓
Data Exploration
      ↓
Text Cleaning
      ↓
Train-Test Split
      ↓
TF-IDF Feature Extraction
      ↓
Train Multiple Models
      ↓
Model Evaluation
      ↓
Best Model Selection
      ↓
Save Model
      ↓
Streamlit Prediction
```

---

## 🖥️ Streamlit Application

A Streamlit web application is included for real-time email classification.

The user can:

1. Enter or paste an email message.
2. Click the **Predict** button.
3. Get the classification result.
4. View whether the email is **SPAM** or **HAM**.

### Example

**Input:**

```text
Congratulations! You have won a free prize.
Click here to claim your reward now!
```

**Output:**

```text
🚨 SPAM
```

Another example:

**Input:**

```text
Hi, please find the meeting details attached.
We will discuss the project tomorrow.
```

**Output:**

```text
✅ HAM
```

---

## 📁 Project Structure

```text
DataScience-Task4-EmailSpamDetection/
│
├── data/
│   └── spam.csv
│
├── notebooks/
│   └── Email_Spam_Detection.ipynb
│
├── models/
│   └── spam_model.pkl
│
├── frontend/
│   └── streamlit_app.py
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
* **Natural Language Processing (NLP)**
* **TF-IDF**
* **Logistic Regression**
* **Multinomial Naive Bayes**
* **Linear SVM**
* **Joblib**
* **Streamlit**
* **Matplotlib**
* **Seaborn**
* **Jupyter Notebook**

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/Gurunathan-16/OIBSIP.git
```

Navigate to the Task 4 directory:

```bash
cd OIBSIP/DataScience-Task4-EmailSpamDetection
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

---

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

## 💾 Saved Model

The final trained Machine Learning pipeline is saved using Joblib:

```text
models/spam_model.pkl
```

The saved pipeline contains the required text vectorization and classification components, allowing new email messages to be directly passed to the model for prediction.

---

## 📏 Evaluation Metrics

The following metrics were used to evaluate the classification models:

### Accuracy

Measures the percentage of correctly classified emails.

### Precision

Measures how many emails predicted as spam were actually spam.

### Recall

Measures how many actual spam emails were correctly detected.

### F1 Score

Provides a balance between Precision and Recall.

For spam detection, Precision, Recall, and F1 Score are particularly important because both false positives and missed spam messages should be considered.

---

## 💡 Key Learning Outcomes

Through this project, I gained practical experience in:

* Natural Language Processing
* Text preprocessing
* TF-IDF feature extraction
* Binary classification
* Logistic Regression
* Naive Bayes
* Linear SVM
* Model evaluation
* Precision, Recall, and F1 Score
* Model serialization using Joblib
* Streamlit application development
* Integrating Machine Learning models into applications

---

## 🚀 Future Improvements

Possible improvements include:

* Training with a larger and more diverse email dataset.
* Advanced NLP preprocessing.
* Hyperparameter tuning.
* Testing transformer-based NLP models.
* Improving detection of sophisticated spam messages.
* Deploying the application online.

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

### Task 4 — Email Spam Detection

#OasisInfobyte #DataScience #MachineLearning #Python #NLP #EmailSpamDetection #Internship
