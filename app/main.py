from fastapi import FastAPI, Request,HTTPException
from fastapi.responses import HTMLResponse
from app.schemas import StockIn
from app.services.data_service import fetch_stock_data
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI(title="Stock Prediction API")
app.mount("/static", StaticFiles(directory="app/static"), name="static")


templates = Jinja2Templates(directory="app/templates")


@app.post("/predict")
async def predict(stock_data: StockIn):
    try:
        df = fetch_stock_data(stock_data.ticker, stock_data.period, stock_data.interval)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    return {"data": df.shape}

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})