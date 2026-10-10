
import streamlit as st
import pandas as pd
import joblib
from pathlib import Path

# --------------------------------------------------
# 1. PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="Customer Churn Intelligence",
    page_icon="📊",
    layout="wide"
)

# --------------------------------------------------
# 2. LOAD SAVED MACHINE LEARNING ARTIFACTS
# --------------------------------------------------

MODEL_PATH = (
    Path(__file__).resolve().parent.parent
    / "models"
    / "churn_artifacts.pkl"
)

st.title("Customer Intelligence & Churn Prediction System")

st.write(
    "Predict customer churn risk, identify customer segments, "
    "and explore potential retention actions."
)

try:
    artifacts = joblib.load(MODEL_PATH)

    log_model = artifacts["model"]
    preprocessor = artifacts["preprocessor"]
    kmeans = artifacts["kmeans"]
    scaler = artifacts["scaler"]
    segmentation_features = artifacts["segmentation_features"]

except Exception as e:
    st.error(f"Unable to load model artifacts: {e}")
    st.stop()

# --------------------------------------------------
# 3. CUSTOMER INPUT FORM
# --------------------------------------------------

st.divider()
st.header("Customer Details")

st.write("Enter the customer's details below to estimate churn risk.")

with st.form("customer_form"):

    col1, col2 = st.columns(2)

    with col1:
        gender = st.selectbox(
            "Gender",
            ["Male", "Female"]
        )

        SeniorCitizen = st.selectbox(
            "Senior Citizen",
            [0, 1],
            format_func=lambda value: "Yes" if value == 1 else "No"
        )

        Partner = st.selectbox(
            "Has Partner?",
            ["Yes", "No"]
        )

        Dependents = st.selectbox(
            "Has Dependents?",
            ["Yes", "No"]
        )

        tenure = st.number_input(
            "Tenure (months)",
            min_value=0,
            max_value=72,
            value=12
        )

        PhoneService = st.selectbox(
            "Phone Service",
            ["Yes", "No"]
        )

        MultipleLines = st.selectbox(
            "Multiple Lines",
            ["No", "Yes", "No phone service"]
        )

        InternetService = st.selectbox(
            "Internet Service",
            ["DSL", "Fiber optic", "No"]
        )

        OnlineSecurity = st.selectbox(
            "Online Security",
            ["No", "Yes", "No internet service"]
        )

        OnlineBackup = st.selectbox(
            "Online Backup",
            ["No", "Yes", "No internet service"]
        )

    with col2:
        DeviceProtection = st.selectbox(
            "Device Protection",
            ["No", "Yes", "No internet service"]
        )

        TechSupport = st.selectbox(
            "Tech Support",
            ["No", "Yes", "No internet service"]
        )

        StreamingTV = st.selectbox(
            "Streaming TV",
            ["No", "Yes", "No internet service"]
        )

        StreamingMovies = st.selectbox(
            "Streaming Movies",
            ["No", "Yes", "No internet service"]
        )

        Contract = st.selectbox(
            "Contract Type",
            ["Month-to-month", "One year", "Two year"]
        )

        PaperlessBilling = st.selectbox(
            "Paperless Billing",
            ["Yes", "No"]
        )

        PaymentMethod = st.selectbox(
            "Payment Method",
            [
                "Electronic check",
                "Mailed check",
                "Bank transfer (automatic)",
                "Credit card (automatic)"
            ]
        )

        MonthlyCharges = st.number_input(
            "Monthly Charges ($)",
            min_value=0.0,
            value=70.0,
            step=5.0
        )

        TotalCharges = st.number_input(
            "Total Charges ($)",
            min_value=0.0,
            value=840.0,
            step=50.0
        )

    submitted = st.form_submit_button(
        "Predict Customer Churn",
        type="primary",
        use_container_width=True
    )

# --------------------------------------------------
# 4. PREDICTION AND CUSTOMER SEGMENTATION
# --------------------------------------------------

if submitted:

    customer_data = {
        "gender": gender,
        "SeniorCitizen": SeniorCitizen,
        "Partner": Partner,
        "Dependents": Dependents,
        "tenure": tenure,
        "PhoneService": PhoneService,
        "MultipleLines": MultipleLines,
        "InternetService": InternetService,
        "OnlineSecurity": OnlineSecurity,
        "OnlineBackup": OnlineBackup,
        "DeviceProtection": DeviceProtection,
        "TechSupport": TechSupport,
        "StreamingTV": StreamingTV,
        "StreamingMovies": StreamingMovies,
        "Contract": Contract,
        "PaperlessBilling": PaperlessBilling,
        "PaymentMethod": PaymentMethod,
        "MonthlyCharges": MonthlyCharges,
        "TotalCharges": TotalCharges
    }

    customer_df = pd.DataFrame([customer_data])

    # Apply the same preprocessing used during training
    processed_customer = preprocessor.transform(customer_df)

    # Predict churn probability
    churn_probability = float(
        log_model.predict_proba(processed_customer)[0, 1]
    )

    # Assign a customer segment
    segment_data = customer_df[segmentation_features]
    scaled_segment = scaler.transform(segment_data)

    cluster = int(kmeans.predict(scaled_segment)[0])

    segment_names = {
        0: "New / Low-Value",
        1: "Loyal / High-Value",
        2: "Newer / High-Spend",
        3: "Loyal / Low-Spend"
    }

    segment_name = segment_names.get(
        cluster,
        f"Cluster {cluster}"
    )

    # --------------------------------------------------
    # 5. DISPLAY RESULTS
    # --------------------------------------------------

    st.divider()
    st.header("Churn Prediction Results")

    probability_pct = churn_probability * 100

    metric1, metric2 = st.columns(2)

    with metric1:
        st.metric(
            "Predicted Churn Risk",
            f"{probability_pct:.2f}%"
        )

    with metric2:
        st.metric(
            "Customer Segment",
            segment_name
        )

    st.progress(churn_probability)

    if churn_probability >= 0.70:
        st.error("HIGH RISK — Prioritize Retention")
        risk_level = "High"

    elif churn_probability >= 0.40:
        st.warning("MEDIUM RISK — Consider Retention Support")
        risk_level = "Medium"

    else:
        st.success("LOW RISK — Continue Regular Engagement")
        risk_level = "Low"

    # --------------------------------------------------
    # 6. RETENTION RECOMMENDATIONS
    # --------------------------------------------------

    st.divider()
    st.header("Recommended Retention Action")

    if risk_level == "High":

        if Contract == "Month-to-month":
            st.write(
                "Consider personalized outreach and an appropriate "
                "longer-term contract incentive."
            )

        elif MonthlyCharges >= 80:
            st.write(
                "Review the customer's billing and check whether "
                "a suitable plan or loyalty offer is available."
            )

        else:
            st.write(
                "Prioritize personal outreach to understand "
                "the customer's concerns."
            )

    elif risk_level == "Medium":

        if Contract == "Month-to-month":
            st.write(
                "Explain the benefits of longer-term plans and "
                "consider an appropriate upgrade incentive."
            )

        elif (
            OnlineSecurity == "No"
            and InternetService != "No"
        ):
            st.write(
                "Consider explaining the available online "
                "security options and their benefits."
            )

        else:
            st.write(
                "Consider a customer satisfaction survey and "
                "review the customer's service experience."
            )

    else:
        st.write(
            "Continue regular customer engagement and monitor "
            "satisfaction."
        )

    st.caption(
        "Churn probabilities are model estimates. Risk thresholds "
        "and retention recommendations are project-defined rules; "
        "they do not guarantee customer retention."
    )

# --------------------------------------------------
# 7. FOOTER
# --------------------------------------------------

st.divider()

st.caption(
    "Customer Intelligence & Churn Prediction System | "
    "Python · Scikit-learn · XGBoost · SHAP · Streamlit"
)
