# 📧 Spam Email Classification using Machine Learning

## 📌 Project Overview
This project builds a **Spam Email Classification System** using Machine Learning and Natural Language Processing (NLP).

The model automatically classifies messages as:
- ✅ **Ham (Not Spam)**  
- ❌ **Spam**

The project demonstrates a complete **end-to-end ML pipeline**, including data preprocessing, feature engineering, model training, evaluation, and comparison.

---

## 🎯 Objective
- Detect spam messages accurately
- Compare multiple machine learning models
- Understand trade-offs between **Accuracy, Precision, and Recall**

---

## 📊 Dataset
- Dataset: **SMS Spam Collection Dataset**
- Total messages: ~5,500
- Classes:
  - Ham → Not Spam
  - Spam → Unwanted messages

---

## 🛠️ Technologies Used

- **Python**
- **Pandas, NumPy**
- **Scikit-learn**
- **NLTK (Natural Language Processing)**
- **Matplotlib / Seaborn**

---

## ⚙️ ML Pipeline

### 1️⃣ Data Preprocessing
- Convert text to lowercase  
- Remove punctuation & special characters  
- Remove stopwords  
- Tokenization & Stemming  

---

### 2️⃣ Feature Engineering
- **TF-IDF Vectorization**
- Converts text → numerical representation

---

### 3️⃣ Model Training

The following models were used:

- ✅ Naive Bayes  
- ✅ Logistic Regression  
- ✅ Support Vector Machine (SVM)  

---

### 4️⃣ Model Evaluation

Metrics used:
- Accuracy  
- Precision  
- Recall  
- F1 Score  
- Confusion Matrix  

---

## 📈 Model Comparison

| Model | Accuracy | Precision | Key Insight |
|------|---------|----------|------------|
| Naive Bayes | ✅ High | ✅ 1.0 | Best for text data |
| Logistic Regression | Moderate | Moderate | Works for structured data |
| ✅ SVM | ✅ High | ✅ Balanced | Best balance (Precision + Recall) |

---

## 🔍 Key Insights

- **Naive Bayes** achieved **100% precision**  
  👉 No false spam predictions  

- **SVM** provided better balance between:
  👉 Precision & Recall  

- **Logistic Regression** performed moderately due to high-dimensional text data

---

## 💡 Business Understanding

- Spam detection requires **high precision**  
- False positives (important emails marked as spam) must be avoided  

👉 So, Naive Bayes is preferred in strict scenarios  
👉 SVM is preferred for balanced performance  

---

## 🚀 Future Improvements

- Add:
  - Random Forest  
  - XGBoost  
  - Deploy using **Flask or Streamlit**

---

## 🧠 Learnings

This project helped in understanding:

- End-to-end ML workflow  
- NLP preprocessing techniques  
- Model selection based on data type  
- Precision vs Recall trade-offs  

---

## ✅ Conclusion

This project demonstrates how different machine learning models behave on text-based data and highlights the importance of choosing the right algorithm based on:

- Data type  
- Feature characteristics  
- Business requirements  

---

## 📌 Author
👤 Manimozhi S  


