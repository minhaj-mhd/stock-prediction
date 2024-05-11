import pandas as pd
import yfinance as yf

def fetch_stock_data(ticker: str, period: str, interval: str) -> pd.DataFrame:
    stock = yf.Ticker(ticker)
    return stock.history(period=period, interval=interval)