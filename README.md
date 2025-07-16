# Hybrid Network Analysis and Machine Learning for Financial Distress Prediction

This project presents a **hybrid model** combining **network analysis** and **machine learning algorithms** to predict **financial distress** in companies. It integrates structured financial data with relational network insights, enabling more accurate, real-time, and data-rich predictions compared to traditional models.

---

## 📘 About the Project

Financial distress prediction is critical for ensuring the stability of businesses and financial institutions. Traditional statistical models, such as the Altman Z-score and logistic regression, often fail to capture the non-linear relationships and real-time dynamics of financial data.

This project proposes a **Hybrid Network Analysis and Machine Learning Model** that:
- Builds a network of financial relationships between companies
- Applies machine learning algorithms for predictive modeling
- Enhances prediction accuracy through multi-source data (financial, market sentiment, etc.)

---

## 🚩 Problem with Existing Systems

Existing financial distress prediction systems suffer from:
- ❌ **Limited Data Scope** – Focused only on numerical ratios
- ❌ **Inability to Model Complex Relationships** – Linear models only
- ❌ **No Real-Time Adaptability** – No live data input handling

---

## ✅ Proposed Solution

Our hybrid system overcomes the limitations by:
- 📊 Using **machine learning classifiers** (Logistic Regression, Decision Tree, KNN, Passive-Aggressive)
- 🌐 Building **network graphs** of financial entities
- 🧠 Integrating both **structured** and **unstructured** data sources
- 🔄 Supporting **real-time adaptability** with dynamic model updates

---

## ⚙️ Technologies Used

- Python
- HTML/CSS (Frontend)
- Flask / Django (Backend Framework)
- Scikit-learn
- Pandas, NumPy
- SQLite (Database)
- NetworkX (for network graph analysis)

---

## 🔍 Machine Learning Algorithms Used

### 1. Logistic Regression
- Probabilistic linear model for binary classification
- Strengths: Interpretable, efficient for structured data
- Limitation: Assumes linearity

### 2. Decision Tree Classifier
- Rule-based model splitting data using entropy/gini
- Strengths: Visual, handles non-linearity
- Limitation: Overfitting on deep trees

### 3. K-Nearest Neighbors (KNN)
- Instance-based model using distance metrics
- Strengths: Simple, flexible decision boundaries
- Limitation: High prediction cost, sensitive to irrelevant features

### 4. Passive-Aggressive Classifier
- Online learning for real-time updates
- Strengths: Suitable for large-scale, sparse data
- Limitation: Sensitive to noise, needs tuning

---

## 📁 Project Structure

├── app/
│ ├── static/ # CSS, images, JS
│ ├── templates/ # HTML pages
│ ├── models.py
│ ├── views.py
├── financial_distress/ # Django or Flask config
├── manage.py / app.py
├── requirements.txt
├── README.md
└── db.sqlite3

yaml
Copy
Edit

---

## 🚀 How to Run the Project

### 1. Clone the Repository
```bash
git clone https://github.com/Kadambari01/Financial-Distress-Prediction.git
cd Financial-Distress-Prediction
2. Install Required Packages
bash
Copy
Edit
pip install -r requirements.txt
3. Run the Web Application
If using Flask:

bash
Copy
Edit
python app.py
If using Django:

bash
Copy
Edit
python manage.py runserver
4. Access the App
Open your browser and go to:

cpp
Copy
Edit
http://127.0.0.1:5000
📈 Advantages of This System
✅ Higher Accuracy by combining network analysis with ML

✅ Handles Structured & Unstructured Data

✅ Real-Time Adaptability

✅ Rich Interpretability using visual network graphs

📚 References
Altman, E.I. (1968). Financial Ratios, Discriminant Analysis and the Prediction of Corporate Bankruptcy.

Research studies on ML for distress prediction [2], [3], [4]

SVM, ANN, and hybrid ML techniques in finance

👨‍💻 Author
Kadambari
GitHub: Kadambari01
