import streamlit as st
import pandas as pd
import joblib
from pathlib import Path

# -----------------------------
# Project paths
# -----------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_PATH = BASE_DIR / "models" / "customer_churn_model.pkl"
PREPROCESSOR_PATH = BASE_DIR / "models" / "preprocessor.pkl"

# -----------------------------
# Load model
# -----------------------------
model = joblib.load(MODEL_PATH)
preprocessor = joblib.load(PREPROCESSOR_PATH)

# -----------------------------
# Page configuration
# -----------------------------
st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📊",
    layout="wide"
)

# -----------------------------
# Load saved model
# -----------------------------
model = joblib.load("models/customer_churn_model.pkl")
preprocessor = joblib.load("models/preprocessor.pkl")

# -----------------------------
# Header
# -----------------------------
st.title("📊 Customer Churn Prediction")
st.write(
    "Enter customer details to predict churn probability and assess customer risk."
)

st.divider()

# -----------------------------
# Customer information
# -----------------------------
st.subheader("👤 Customer Information")

col1, col2 = st.columns(2)

with col1:
    gender = st.selectbox(
        "Gender",
        ["Male", "Female"]
    )

    senior_citizen = st.selectbox(
        "Senior Citizen",
        [0, 1]
    )

    partner = st.selectbox(
        "Partner",
        ["Yes", "No"]
    )

    dependents = st.selectbox(
        "Dependents",
        ["Yes", "No"]
    )

with col2:
    tenure = st.number_input(
        "Tenure (months)",
        min_value=0,
        max_value=100,
        value=12
    )

    monthly_charges = st.number_input(
        "Monthly Charges",
        min_value=0.0,
        value=70.0
    )

    total_charges = st.number_input(
        "Total Charges",
        min_value=0.0,
        value=840.0
    )

# -----------------------------
# Services
# -----------------------------
st.subheader("📱 Services")

col1, col2 = st.columns(2)

with col1:
    phone_service = st.selectbox(
        "Phone Service",
        ["Yes", "No"]
    )

    multiple_lines = st.selectbox(
        "Multiple Lines",
        ["Yes", "No", "No phone service"]
    )

    internet_service = st.selectbox(
        "Internet Service",
        ["DSL", "Fiber optic", "No"]
    )

    online_security = st.selectbox(
        "Online Security",
        ["Yes", "No", "No internet service"]
    )

    online_backup = st.selectbox(
        "Online Backup",
        ["Yes", "No", "No internet service"]
    )

with col2:
    device_protection = st.selectbox(
        "Device Protection",
        ["Yes", "No", "No internet service"]
    )

    tech_support = st.selectbox(
        "Tech Support",
        ["Yes", "No", "No internet service"]
    )

    streaming_tv = st.selectbox(
        "Streaming TV",
        ["Yes", "No", "No internet service"]
    )

    streaming_movies = st.selectbox(
        "Streaming Movies",
        ["Yes", "No", "No internet service"]
    )


# Contract and billing

st.subheader("💳 Contract & Billing")

col1, col2 = st.columns(2)

with col1:
    contract = st.selectbox(
        "Contract",
        ["Month-to-month", "One year", "Two year"]
    )

    paperless_billing = st.selectbox(
        "Paperless Billing",
        ["Yes", "No"]
    )

with col2:
    payment_method = st.selectbox(
        "Payment Method",
        [
            "Electronic check",
            "Mailed check",
            "Bank transfer (automatic)",
            "Credit card (automatic)"
        ]
    )

# -----------------------------
# Prediction
# -----------------------------
st.divider()

if st.button("🔮 Predict Customer Churn", use_container_width=True):

    new_customer = pd.DataFrame({
        "gender": [gender],
        "SeniorCitizen": [senior_citizen],
        "Partner": [partner],
        "Dependents": [dependents],
        "tenure": [tenure],
        "PhoneService": [phone_service],
        "MultipleLines": [multiple_lines],
        "InternetService": [internet_service],
        "OnlineSecurity": [online_security],
        "OnlineBackup": [online_backup],
        "DeviceProtection": [device_protection],
        "TechSupport": [tech_support],
        "StreamingTV": [streaming_tv],
        "StreamingMovies": [streaming_movies],
        "Contract": [contract],
        "PaperlessBilling": [paperless_billing],
        "PaymentMethod": [payment_method],
        "MonthlyCharges": [monthly_charges],
        "TotalCharges": [total_charges]
    })
    prediction = model.predict(new_customer)[0]
    probability = model.predict_proba(new_customer)[0][1]

    # -----------------------------
    # Risk level
    # -----------------------------
    if probability < 0.30:
        risk_level = "Low Risk"
    elif probability < 0.70:
        risk_level = "Medium Risk"
    else:
        risk_level = "High Risk"

    # -----------------------------
    # Display result
    # -----------------------------
    st.subheader("📈 Prediction Result")

    col1, col2, col3 = st.columns(3)

    with col1:
        if prediction == 1:
            st.error("⚠️ CHURN")
        else:
            st.success("✅ NO CHURN")

    with col2:
        st.metric(
            "Churn Probability",
            f"{probability:.2%}"
        )

    with col3:
        st.metric(
            "Risk Level",
            risk_level
        )

    # -----------------------------
    # Recommendations
    # -----------------------------
    st.subheader("💡 Recommended Actions")

    if risk_level == "High Risk":

        recommendations = [
            "Contact the customer immediately",
            "Offer a personalized retention discount",
            "Provide technical/customer support",
            "Consider a suitable plan upgrade or incentive"
        ]

    elif risk_level == "Medium Risk":

        recommendations = [
            "Monitor customer activity",
            "Offer personalized support",
            "Provide suitable service recommendations"
        ]

    else:

        recommendations = [
            "No immediate retention action required",
            "Continue regular customer engagement"
        ]

    for action in recommendations:
        st.write(f"• {action}")