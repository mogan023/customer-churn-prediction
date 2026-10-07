# 📊 Customer Churn Prediction

An end-to-end Machine Learning project that predicts whether a telecom customer is likely to churn and estimates their churn probability and risk level.

🔗 **Live Demo:** https://customer-churn-prediction-01.streamlit.app/

🔗 **GitHub Repository:** https://github.com/mogan023/customer-churn-prediction

---

## 🚀 Project Overview

Customer churn is a major challenge for subscription-based businesses. Identifying customers who are likely to leave allows businesses to take proactive retention actions.

This project uses Machine Learning to analyze customer information and predict:

- Whether a customer is likely to churn
- Churn probability
- Customer risk level
- Recommended retention actions

The trained ML model is integrated with a Streamlit web application and deployed online using Streamlit Community Cloud.

---

## 🎯 Objectives

- Understand customer churn patterns
- Perform data preprocessing and exploratory data analysis
- Train a Machine Learning classification model
- Build a prediction pipeline
- Estimate individual customer churn probability
- Categorize customers based on risk
- Provide actionable recommendations
- Deploy the application as a web application

---

## ✨ Key Features

### 🔹 Customer Information
The application accepts customer details such as:

- Gender
- Senior Citizen status
- Tenure
- Monthly Charges
- Total Charges
- And other customer-related attributes

### 🔹 Churn Prediction

The trained Machine Learning model predicts whether the customer is likely to churn.

### 🔹 Churn Probability

The application displays the probability of customer churn as a percentage.

### 🔹 Risk Classification

Customers are classified into three risk levels:

| Churn Probability | Risk Level |
|---|---|
| < 30% | 🟢 Low Risk |
| 30% – <70% | 🟡 Medium Risk |
| ≥ 70% | 🔴 High Risk |

### 🔹 Recommended Actions

Based on the prediction, the application provides suggested customer-retention actions such as:

- Monitor customer activity
- Offer personalized support
- Provide suitable service recommendations

---

## 🧠 Machine Learning Workflow

```text
Raw Customer Data
        ↓
Data Understanding
        ↓
Data Cleaning & Preprocessing
        ↓
Exploratory Data Analysis
        ↓
Feature Preparation
        ↓
Model Training
        ↓
Model Evaluation
        ↓
Model Serialization
        ↓
Streamlit Application
        ↓
Customer Churn Prediction
        ↓
Risk Assessment
        ↓
Recommended Actions
