from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import numpy as np
import pandas as pd
import joblib
import os

# Loading DataSet
if not os.path.exists("company_esg_financial_dataset.csv"):
    raise FileNotFoundError("company_esg_financial_dataset.csv. Please include it for lag computation.")
financial_df = pd.read_csv("company_esg_financial_dataset.csv")

# Loading model and scaler
model = joblib.load("backend/model/xgb_model.pkl")
scaler = joblib.load("backend/model/scaler.pkl")


class InputData(BaseModel):
    CompanyName: str
    Revenue: float
    MarketCap: float
    GrowthRate: float
    WaterUsage: float
    Year: int


app = FastAPI()


@app.post("/predict")
def predict(data: InputData):
    if data.MarketCap == 0:
        raise HTTPException(status_code=400, detail="MarketCap cannot be zero.")
    RevenuePerCap = data.Revenue/data.MarketCap

    if data.Revenue == 0:
        raise HTTPException(status_code=400, detail="Revenue can't be zero")
    WaterPerRevenue = data.WaterUsage/data.Revenue

    prev_year = data.Year - 1
    row = financial_df[(financial_df["CompanyName"] == data.CompanyName) &
                       (financial_df["Year"] == prev_year)]

    if row.empty:
        raise HTTPException(status_code=400,
                            detail="Previous year's revenue not found for this company.")
    Revenue_lag1 = row.iloc[0]["Revenue"]

    features = np.array([[data.Year, data.MarketCap, data.GrowthRate, data.WaterUsage,
                          Revenue_lag1, RevenuePerCap, WaterPerRevenue]])

    x = scaler.transform(features)
    return {"predicted_revenue": float(model.predict(x))}
