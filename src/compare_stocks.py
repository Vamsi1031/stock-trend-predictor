import streamlit as st
import numpy as np
from tensorflow.keras.models import load_model
import os
import plotly.graph_objects as go
from src.data_loader import download_stock_data
from src.preprocessing import preprocess_data
from src.model import build_lstm_model
from src.advisor import analyze_trend, volatility_index
from sklearn.metrics import mean_squared_error, mean_absolute_error

def compare_stocks(ticker_list):
    fig = go.Figure()
    
    for ticker in ticker_list:
        save_path = f"data/{ticker}_data.csv"
        model_path = f"data/{ticker}_model.h5"
        
        df = download_stock_data(ticker, "2019-01-01", "2024-12-31", save_path=save_path)
        if df.empty:
            st.warning(f"⚠️ No data for {ticker}. Skipping.")
            continue
        
        X, y, scaler = preprocess_data(df)

        if os.path.exists(model_path):
            model = load_model(model_path)
        else:
            model = build_lstm_model((X.shape[1], X.shape[2]))
            model.fit(X, y, epochs=5, batch_size=32, verbose=0)
            model.save(model_path)

        predicted = model.predict(X)
        predicted_prices = scaler.inverse_transform(predicted)
        actual_prices = scaler.inverse_transform(y)

        # Plotting line
        fig.add_trace(go.Scatter(
            y=predicted_prices.flatten(), mode='lines', name=f"{ticker} Prediction"
        ))

        # Metrics
        rmse = np.sqrt(mean_squared_error(actual_prices, predicted_prices))
        mae = mean_absolute_error(actual_prices, predicted_prices)

        st.markdown(f"### 📊 {ticker} Results")
        st.write(f"**RMSE:** {rmse:.2f}, **MAE:** {mae:.2f}")

        last_7 = predicted_prices[-7:].flatten()
        st.write("📆 Last 7-Day Predicted Prices:")
        for i, p in enumerate(last_7):
            st.write(f"Day {i+1}: ${p:.2f}")

        st.markdown("💡 **Advice:**")
        st.info(analyze_trend(last_7))
        st.markdown(f"📉 **Volatility:** {volatility_index(last_7):.2f}")
        st.divider()

    # Show combined prediction chart
    fig.update_layout(
        title="📈 Stock Comparison - Predicted Price Trends",
        xaxis_title="Days", yaxis_title="Price",
        height=600
    )
    st.plotly_chart(fig, use_container_width=True)
 
