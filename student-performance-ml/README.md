<<<<<<< HEAD
# ml-algorithms-from-scratch
End-to-end implementation of Machine Learning algorithms from scratch and using scikit-learn
=======
# 🎓 Student Performance Prediction (Machine Learning Project)
 
## 📌 Problem Statement
 
The objective of this project is to predict student **math scores** based on demographic and academic factors such as gender, parental education, lunch type, and test preparation.
 
---
 
## 📊 Dataset
 
* Source: Kaggle - Students Performance in Exams
* Number of records: 1000
* Features include:
 
  * Gender
  * Race/Ethnicity
  * Parental Level of Education
  * Lunch
  * Test Preparation Course
  * Math, Reading, Writing Scores
 
---
 
## 🧠 Approach
 
### 1. Data Loading
 
* Loaded dataset using **DuckDB + SQL queries**
* Built reusable `data_loader.py`
 
### 2. Exploratory Data Analysis (EDA)
 
* Checked data distribution, missing values, and feature relationships
* Identified patterns in student performance
 
### 3. Data Preprocessing
 
* Handled categorical variables using **One-Hot Encoding**
* Split dataset into training and testing sets (80/20)
 
### 4. Model Training
 
Two models were implemented:
 
* **Linear Regression** (baseline model)
* **Random Forest Regressor** (improved model)
 
---
 
## 📊 Model Performance
 
| Model             | R² Score              | RMSE        |
| ----------------- | --------------------- | ----------- |
| Linear Regression | ~0.88                 | ~5.3        |
| Random Forest     | Improved       (~0.85)| ~6.0        |
 
👉 Random Forest performed better by capturing non-linear relationships.
 
---
 
## 🔍 Key Insights
 
* Test preparation significantly improves student performance
* Lunch type (proxy for economic status) impacts scores
* Reading and writing scores are strongly correlated
* Some demographic factors have lower influence
 

 
## ⚙️ Project Structure
 
```text
student-performance-ml/
│
├── data/
│   ├── raw/
│   │   └── StudentsPerformance.csv
│   └── processed/
│
├── notebooks/
│   ├── 01_eda.ipynb
│   ├── 02_data_cleaning.ipynb
│   ├── 03_feature_engineering.ipynb
│   └── 04_model_training.ipynb
│
├── src/
│   ├── data_loader.py
│   └── train.py
│
├── models/
│   └── model.pkl
│
├── requirements.txt
├── README.md
└── .gitignore

 
---
 
## 🚀 How to Run the Project
 
### 1. Clone the repository
 
```
git clone <repo-link>
cd student-performance-ml
```
 
### 2. Create virtual environment
 
```
python -m venv venv
venv\Scripts\activate
```
 
### 3. Install dependencies
 
```
pip install -r requirements.txt
```
 
### 4. Train model
 
```
python src/train.py
```
 
---
 
## 💾 Model Output
 
* Trained model is saved as:
 
```
models/model.pkl
```
 
---
 
## 🧠 Key Concepts Used
 
* Regression Modeling
* Feature Engineering
* One-Hot Encoding
* Train-Test Split
* Model Evaluation (R², RMSE)
* Ensemble Learning (Random Forest)
 
---
 
## 🔮 Future Improvements
 
* Add Cross Validation
* Hyperparameter tuning
* Deploy model using Flask / FastAPI
* Build dashboard for visualization
 
---
 
## 👨‍💻 Author
Manimozhi S
 
>>>>>>> 1764114 (Added student performance ML project)
