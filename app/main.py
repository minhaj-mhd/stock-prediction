from fastapi import FastAPI
from app.schemas import StockIn
app = FastAPI(title="Stock Prediction API")

@app.post("/predict")
async def predict(stock_data: StockIn):
    return {"prediction": "Not implemented"}