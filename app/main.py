from fastapi import FastAPI

app = FastAPI(title="Stock Prediction API")

@app.get("/")
async def root():
    return {"message": "Welcome to Stock Prediction API"}