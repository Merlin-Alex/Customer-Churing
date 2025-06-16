# Customer Churn Prediction – Classification
---
This project focuses on predicting customer churn using classification techniques. The goal is to identify customers who are likely to stop using a service, helping businesses take proactive steps to retain them.

## Problem Statement:
Customer churn directly affects business revenue. By predicting which customers are at risk of leaving, companies can take timely actions like offering discounts or improving service quality
Project Overview

## Dataset:
Source: Telco Customer Churn – Kaggle (https://www.kaggle.com/blastchar/telco-customer-churn)
Includes: Customer demographics, contract details, services used, and billing info.
---
## Project Workflow
### Data Exploration: 
Looked at feature types, shapes, and summary stats. Found that TotalCharges was numerical but stored as object.

### Data Cleaning:
- Handled missing and blank values (e.g., 11 blanks in TotalCharges replaced with 0).
- Removed irrelevant features like CustomerID.

### Preprocessing:
- Replaced "No internet service"/"No phone service" with "No".
- One-hot encoded categorical features.
- Standardized continuous features.
  
### Feature Selection:
- Explored: Mutual Information, RFE, Lasso, and Random Forest-based selection.
  
### Class Imbalance Handling:
- Explored SMOTE, SMOTE+Tomek, ADASYN, and class weighting.

### Model Building:
- Trained multiple classification models.
- Final evaluation focused on Logistic Regression, with and without threshold optimization.
- Other models like Random Forest, XGBoost, and SVM were also tested (see notebook for full details).

### Threshold Optimization:
- Tuned probability thresholds for better business-aligned results.
---
## Results Summary:  
### Model Variants:
1. Default Model (No Balancing, All Features)
- Model: Logistic Regression
- Accuracy: 82%
- Precision (Churn): 0.70
- Recall (Churn): 0.59
- F1 Score (Churn class): 0.64
Highlights: Best accuracy, balanced performance across classes.

 2. Threshold-Optimized Model (Threshold = 0.32)
- Model: Logistic Regression
- Accuracy: 78%
- Precision (Churn): 0.57
- Recall (Churn): 0.79
- F1 Score (Churn): 0.66
Highlights: Better at identifying churners, useful if reducing customer loss is top priority.

## Business Alignment:
- Use the Default Model if overall accuracy and stability are most important.
- Use the Threshold-Optimized Model if the goal is to catch as many churners as possible, even at the cost of precision.
---

##  Model Comparison

| Model Variant             | Accuracy	| Precision (Churn)   | Recall (Churn)    | F1 Score (Churn)  |
|---------------------------|-----------|---------------------|-------------------|-------------------|
| Default Model             | 0.82      | 0.70                | 0.59              | 0.64              |
| Threshold-Optimized Model | 0.78      | 0.57                | 0.79              | 0.66              |

> *Note: Metrics may vary based on data splits and random seed.*

## 🛠️ Tools & Libraries

- Python (Pandas, NumPy)
- Scikit-learn
- XGBoost
- Matplotlib / Seaborn
- imbalanced-learn (SMOTE, ADASYN)
---
###  License:
The contents of this repository are my own work completed during my independent learning. Redistribution, use, or modification without explicit written permission is prohibited.

