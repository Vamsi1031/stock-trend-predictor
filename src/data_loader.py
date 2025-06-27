import yfinance as yf
import pandas as pd
import os

def download_stock_data(ticker, start_date, end_date, save_path="data/stock_data.csv"):
    print(f"Downloading {ticker} data from {start_date} to {end_date}...")
    data = yf.download(ticker, start=start_date, end=end_date)
    if data.empty:
        print("⚠️ No data downloaded.")
        return pd.DataFrame()
    data.to_csv(save_path)
    return data