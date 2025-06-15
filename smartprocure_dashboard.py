
import streamlit as st
import pandas as pd
import joblib
import numpy as np
import matplotlib.pyplot as plt

# Load trained models
rf_classifier = joblib.load("rf_classifier.pkl")
rf_regressor = joblib.load("rf_regressor.pkl")

st.set_page_config(page_title="SmartProcure Dashboard", layout="centered")
st.title("📦 SmartProcure: Procurement Intelligence System")
st.markdown("Predict procurement **Kraljic category** and estimate **lead time** based on item features.")

with st.form("form"):
    st.subheader("Enter Procurement Item Details")
    lead_time = st.slider("Lead Time (days)", 1, 180, 30)
    order_volume = st.number_input("Order Volume", 1, value=1000)
    cost_per_unit = st.number_input("Cost per Unit ($)", 0.01, value=250.00)
    supply_risk = st.slider("Supply Risk Score (1–5)", 1, 5, 3)
    profit_impact = st.slider("Profit Impact Score (1–5)", 1, 5, 4)
    environmental_impact = st.slider("Environmental Impact Score (1–5)", 1, 5, 3)
    submitted = st.form_submit_button("Predict")

if submitted:
    input_data = pd.DataFrame([{
        'Lead_Time_Days': lead_time,
        'Order_Volume_Units': order_volume,
        'Cost_per_Unit': cost_per_unit,
        'Supply_Risk_Score': supply_risk,
        'Profit_Impact_Score': profit_impact,
        'Environmental_Impact': environmental_impact
    }])
    features = ['Lead_Time_Days', 'Order_Volume_Units', 'Cost_per_Unit',
                'Supply_Risk_Score', 'Profit_Impact_Score', 'Environmental_Impact']
    predicted_category = rf_classifier.predict(input_data[features])[0]
    predicted_lead_time = rf_regressor.predict(input_data[features])[0]

    st.success(f"🧠 Predicted Kraljic Category: {predicted_category}")
    st.info(f"⏳ Predicted Lead Time: {round(float(predicted_lead_time), 2)} days")

    # Feature importance
    st.subheader("🔍 Feature Importance")
    importances = rf_classifier.feature_importances_
    sorted_idx = np.argsort(importances)
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.barh(np.array(features)[sorted_idx], importances[sorted_idx], color='teal')
    ax.set_xlabel("Importance")
    ax.set_title("Top Features Influencing Category Classification")
    st.pyplot(fig)
