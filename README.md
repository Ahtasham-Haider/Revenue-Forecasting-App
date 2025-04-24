# 📈 Revenue Forecasting Web App

This project is a full-stack ML application for predicting a company's future revenue using ESG and financial data.

---

## 🧠 Model
Trained using XGBoost on the ESG & Financial Performance Dataset from Kaggle.  
The model uses features such as:
- Year
- MarketCap
- GrowthRate
- WaterUsage
- Engineered features:
  - Revenue_lag1 (previous year's revenue)
  - RevenuePerCap (Revenue / MarketCap)
  - WaterPerRevenue (WaterUsage / Revenue)

---

## 🖥️ Tech Stack
- **Backend**: FastAPI (served using Uvicorn)
- **Frontend**: Streamlit
- **Modeling**: XGBoost + Scikit-learn
- **Data**: `company_esg_financial_dataset.csv`

---

## 🚀 How to Run

1. **Clone repo & navigate** to the folder:
    ```bash
    cd 1_Revenue_forecasting_project
    ```

2. **(Optional)** Create virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Start backend server**:
    ```bash
    uvicorn backend.main:app --reload
    ```

5. **Run frontend app**:
    ```bash
    streamlit run frontend/app.py
    ```

---

## 📝 Notes
- Ensure `company_esg_financial_dataset.csv` is placed in the `backend/` folder.
- Model (`xgb_model.pkl`) and scaler (`scaler.pkl`) should also be under `backend/model/`.

---

## 🧑‍💻 Author
Built with ❤️ by **Ahtasham Haider**
