from fastapi import FastAPI
from app.schemas import StockIn
from app.services.data_service import fetch_stock_data

app = FastAPI(title="Stock Prediction API")

@app.post("/predict")
async def predict(stock_data: StockIn):
    df = fetch_stock_data(stock_data.ticker, stock_data.period, stock_data.interval)
    return {"data": df.shape}