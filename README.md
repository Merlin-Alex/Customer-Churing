# Customer Churn Prediction – Classification

This project focuses on predicting customer churn using classification techniques. The goal is to identify customers who are likely to stop using a service, helping businesses take proactive steps to retain them.

## Problem Statement:
Customer churn directly affects business revenue. By predicting which customers are at risk of leaving, companies can take timely actions like offering discounts or improving service quality
Project Overview

## Dataset:
Source: Telco Customer Churn – Kaggle(https://www.kaggle.com/blastchar/telco-customer-churn)
Includes: Customer demographics, contract details, services used, and billing info.

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
- Tuned probability thresholds for better business-aligned results. The threshold of 0.38 was chosen based on maximizing the F1-score from the precision-recall curve. This approach balances precision and recall to optimize the model’s ability to identify churners effectively.

## Results Summary:  
### Model Variants:
1. Default Model (No Balancing, All Features)
- Model: Logistic Regression
- Accuracy: 82%
- Precision (Churn): 0.70
- Recall (Churn): 0.59
- F1 Score (Churn class): 0.64
Highlights: Highest overall accuracy with balanced performance across both churn and non-churn classes.

 2. Threshold-Optimized Model (Threshold = 0.32)
- Model: Logistic Regression
- Accuracy: 81%
- Precision (Churn): 0.62
- Recall (Churn): 0.72
- F1 Score (Churn): 0.67
Highlights: Improved ability to identify churners (higher recall), making it valuable when reducing customer loss is the top priority.

## Business Alignment:
- Use the Default Model if overall accuracy and stability are critical.
- Use the Threshold-Optimized Model if the goal is to catch as many churners as possible, even at the cost of precision.


##  Model Comparison for Logistic Regression(LR)

| Model Variant - LR        | Accuracy	| Precision (Churn)   | Recall (Churn)    | F1 Score (Churn)  |
|---------------------------|-----------|---------------------|-------------------|-------------------|
| Default Model             | 0.82      | 0.70                | 0.59              | 0.64              |
| Threshold-Optimized Model | 0.81      | 0.62                | 0.72              | 0.67              |

> *Note: Metrics may vary based on data splits and random seed.*

## 🛠️ Tools & Libraries

- Python (Pandas, NumPy)
- Scikit-learn
- XGBoost
- Matplotlib / Seaborn
- imbalanced-learn (SMOTE, ADASYN)

###  License:
The contents of this repository are my own work completed during my independent learning. Redistribution, use, or modification without explicit written permission is prohibited.

