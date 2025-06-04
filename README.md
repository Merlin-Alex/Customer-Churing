# Customer-Churing

# 🧾 Customer Churn Prediction – Classification & Regression

This repository contains a comprehensive analysis and modeling pipeline for predicting **customer churn**, using both **classification** (predicting if a customer will churn) and **regression** (predicting how long until a customer churns).

---

## 📌 Project Overview

Customer churn is a critical metric for businesses seeking to retain customers and improve lifetime value. This project tackles churn prediction using:

- **Binary Classification**: Will a customer churn? (Yes/No)
- **Regression**: How long until a customer is likely to churn? (Time-based estimation)

The project uses the **Telco Customer Churn dataset** as the foundation for exploratory data analysis (EDA), preprocessing, and modeling.

---

## 🧠 Machine Learning Techniques

### 🔹 Classification Models
- Logistic Regression
- Random Forest
- XGBoost Classifier
- Support Vector Machine (SVM)

### 🔹 Regression Models
- Linear Regression
- XGBoost Regressor
- Random Forest Regressor

---

## 📊 Dataset

**Dataset Used**: [Telco Customer Churn Dataset (Kaggle)](https://www.kaggle.com/blastchar/telco-customer-churn)

The dataset contains customer demographic information, service subscription details, and account data. It has been preprocessed to handle missing values, categorical encoding, and class imbalance.

---

## 📈 Results Summary

| Task           | Best Model         | Key Metric         | Score    |
|----------------|--------------------|---------------------|----------|
| Classification | XGBoost Classifier | F1 Score            | 0.82     |
| Regression     | XGBoost Regressor  | RMSE                | 2.31     |

> 📌 *Note: Results may vary depending on train-test split and hyperparameter tuning.*

---

## 🧪 Key Steps

- 🔍 **Exploratory Data Analysis (EDA)**
- 🧹 **Data Cleaning & Encoding**
- ⚖️ **Handling Class Imbalance (SMOTE / Oversampling)**
- 🧮 **Feature Engineering**
- 🧪 **Model Training & Evaluation**
- 📊 **Model Comparison**

---

## 🛠️ Tools & Libraries

- Python (Pandas, NumPy)
- Scikit-learn
- XGBoost
- Matplotlib / Seaborn
- SMOTE (from imbalanced-learn)

---

## 📄 Folder Structure

