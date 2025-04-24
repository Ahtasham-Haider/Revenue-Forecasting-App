import streamlit as st
import requests

st.title("Welcome! This is a Revenue prediction APP")
st.sidebar.header("**Dash-Board**")
select = st.sidebar.radio("Select", ["About", "Model-Info", "Predict Revenue"])
if select == "About":
    st.subheader("This is a demo app for revenue prediction.")
    st.write("Built by Ahtasham Haider")

elif select == "Model-Info":
    st.markdown("**This app is using Random forest model trained on**"
                " _company_esg_financial_dataset.csv_ **available on kaggle website**")
    st.markdown("for more details, please visit [kaggle]"
                "(https://www.kaggle.com/datasets/shriyashjagtap/esg-and-financial-performance-dataset)")

else:
    st.subheader("Please provide the following details")
    CompanyName = st.text_input("Company Name")
    Revenue = st.number_input("Revenue")
    MarketCap = st.number_input("Market Cap")
    GrowthRate = st.number_input("Growth Rate")
    WaterUsage = st.number_input("Water Usage")
    Year = st.slider("Year", 2015, 2025, 2022)

    input_data = {
        "CompanyName": CompanyName,
        "Revenue": Revenue,
        "MarketCap": MarketCap,
        "GrowthRate": GrowthRate,
        "WaterUsage": WaterUsage,
        "Year": Year
    }

    if st.button("Predict"):
        response = requests.post("https://revenue-backend.onrender.com/predict", json=input_data)
        if response.status_code == 200:
            prediction = response.json()["predicted_revenue"]
            st.success(f"📊 Predicted Revenue: ₹{prediction:,.2f}")
        else:
            st.error("Prediction failed. Check backend.")

