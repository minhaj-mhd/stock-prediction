from pydantic import BaseModel

class StockIn(BaseModel):
    ticker: str
    period: str = "1y"
    interval: str = "1d"