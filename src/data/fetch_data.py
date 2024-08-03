# src/data/fetch_data.py

import yfinance as yf

def fetch_real_time_price(ticker):
    stock = yf.Ticker(ticker)
    return stock.history(period="1d")['Close'].iloc[0]
