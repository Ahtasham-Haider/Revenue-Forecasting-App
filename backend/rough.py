# # File: main.py
# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel
# import numpy as np
# import pandas as pd
# import joblib
# import os
#
# # Load model and scaler
# model = joblib.load("xgb_model.pkl")
# scaler = joblib.load("scaler.pkl")
#
# # Load historical revenue data to compute Revenue_lag1
# # This file should be saved during training
# if not os.path.exists("historical_revenue.csv"):
#     raise FileNotFoundError("historical_revenue.csv not found. Please include it for lag computation.")
# historical_df = pd.read_csv("historical_revenue.csv")
#
#
# # Define the input schema
# class InputData(BaseModel):
#     CompanyName: str
#     Year: int
#     MarketCap: float
#     GrowthRate: float
#     WaterUsage: float
#     Revenue: float  # Current year's Revenue (needed for engineered features)
#
#
# app = FastAPI()
#
#
# @app.post("/predict")
# def predict(data: InputData):
#     # Compute RevenuePerCap
#     if data.MarketCap == 0:
#         raise HTTPException(status_code=400, detail="MarketCap cannot be zero.")
#     RevenuePerCap = data.Revenue / data.MarketCap
#
#     # Compute WaterPerRevenue
#     if data.Revenue == 0:
#         raise HTTPException(status_code=400, detail="Revenue cannot be zero.")
#     WaterPerRevenue = data.WaterUsage / data.Revenue
#
#     # Compute Revenue_lag1 from historical data
#     prev_year = data.Year - 1
#     row = historical_df[(historical_df['CompanyName'] == data.CompanyName) &
#                         (historical_df['Year'] == prev_year)]
#     if row.empty:
#         raise HTTPException(status_code=404, detail="Previous year's revenue not found for this company.")
#     Revenue_lag1 = row.iloc[0]['Revenue']
#
#     # Create final feature array
#     features = np.array([[data.Year, data.MarketCap, data.GrowthRate, data.WaterUsage,
#                           Revenue_lag1, RevenuePerCap, WaterPerRevenue]])
#
#     # Apply scaling
#     scaled = scaler.transform(features)
#
#     # Predict
#     prediction = model.predict(scaled)[0]
#     return {"predicted_revenue": float(prediction)}



# {
#   "CompanyName": "Company_1",
#   "Revenue": 593.2,
#   "MarketCap": 248.400,
#   "GrowthRate": -1.8,
#   "WaterUsage": 21268.2,
#   "Year": 2022
# }