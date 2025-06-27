
import numpy as np
import pandas as pd
import yfinance as yf
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM

def download_data(ticker, start='2019-01-01', end='2024-12-31'):
    df = yf.download(ticker, start=start, end=end)
    df.to_csv('data/stock_data.csv')
    return df

def preprocess_data(df, window_size=60):
    close_prices = df['Close'].values.reshape(-1, 1)
    scaler = MinMaxScaler()
    scaled_data = scaler.fit_transform(close_prices)

    X = []
    y = []

    for i in range(window_size, len(scaled_data)):
        X.append(scaled_data[i - window_size:i])
        y.append(scaled_data[i])

    X, y = np.array(X), np.array(y)
    return X, y, scaler

def build_model(input_shape):
    model = Sequential()
    model.add(LSTM(50, return_sequences=True, input_shape=input_shape))
    model.add(LSTM(50))
    model.add(Dense(1))
    model.compile(optimizer='adam', loss='mean_squared_error')
    return model

def run_stock_prediction(ticker):
    try:
        df = download_data(ticker)
        X, y, scaler = preprocess_data(df)

        model = build_model((X.shape[1], 1))
        model.fit(X, y, epochs=10, batch_size=32, verbose=0)

        # Future forecasting (e.g., next 30 days)
        input_data = X[-1:].copy()
        predicted_prices = []

        for _ in range(30):
            next_price = model.predict(input_data, verbose=0)
            predicted_prices.append(next_price[0])

            # Fix: reshape next_price before appending to input_data
            input_data = np.append(input_data[:, 1:, :], [[[next_price[0][0]]]], axis=1)

        predicted_prices = scaler.inverse_transform(predicted_prices)
        return model, X, scaler, predicted_prices

    except Exception as e:
        print("Prediction error:", e)
        return None, None, None, None
