 
 
import yfinance as yf
from src.run_predictor import run_stock_prediction

def get_top_stocks(tickers):
    results = []

    for ticker in tickers:
        try:
            model, X, scaler, predicted = run_stock_prediction(ticker)

            if model and predicted is not None and len(predicted) > 2:
                trend = predicted[-1] - predicted[-2]
                suggestion = "✅ Buy" if trend > 0 else "⚠️ Hold"
                results.append({
                    "ticker": ticker,
                    "trend_value": trend,
                    "suggestion": suggestion,
                    "predicted_prices": predicted[-30:].flatten()
                })
        except Exception as e:
            print(f"Error for {ticker}: {e}")

    results.sort(key=lambda x: x["trend_value"], reverse=True)
    return results[:5]
