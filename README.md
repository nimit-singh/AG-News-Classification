# 📰 AG News Classification using Machine Learning

A Machine Learning-based web application that classifies news articles into predefined categories such as **World, Sports, Business, and Sci/Tech**.
The project includes both **manual prediction** and **bulk CSV classification** using an interactive Streamlit interface.

---

## 🚀 Features

* 🔹 Classify news into 4 categories:

  * 🌍 World
  * 🏆 Sports
  * 💼 Business
  * 💻 Sci/Tech

* 🔹 **Manual Prediction**

  * Enter title + description
  * Get instant result

* 🔹 **Bulk Scanner**

  * Upload CSV file
  * Classify multiple news articles at once

* 🔹 Clean and simple Streamlit UI

* 🔹 Fast predictions using trained ML model

---

## 📂 Project Structure

```
AG-News-Classification/
│
├── Data/                                 # Dataset
├── pages/                                # Streamlit pages (Bulk Scanner)
├── main.py                               # Main Streamlit app
├── Manual_Prediction.py                  # Manual prediction logic
├── News_Classification_Model_LR.joblib   # Trained ML model
├── AG_News_Classification.ipynb          # Model training notebook
├── Report.pdf                            # Project report
├── presentation.pdf                      # Presentation
├── requirements.txt                      # Dependencies
└── README.md                             # Documentation
```

---

## 🧠 Model Information

* **Algorithm:** Logistic Regression
* **Vectorization:** TF-IDF
* **Dataset:** AG News Dataset
* **Task:** Multi-class Text Classification

---

## 🛠️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/nimit-datahub/AG-News-Classification.git
cd AG-News-Classification
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
streamlit run main.py
```

---

## 📊 How to Use

### 🔹 Manual Prediction

* Enter **news title**
* Enter **description**
* Click predict to get category

### 🔹 Bulk Scanner

* Upload a CSV file
* Required format:

```
Title,Description
Stock market rises,Investors are optimistic about growth
Football match ends,Team wins championship
```

---

## 📸 Screenshots



---

## 📈 Future Improvements

* 🔹 Add Deep Learning models (LSTM / BERT)
* 🔹 Improve accuracy with better preprocessing
* 🔹 Deploy application online
* 🔹 Add real-time news API integration

---

## 👨‍💻 Author

**Nimit Singh**

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub!
