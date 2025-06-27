from src.run_predictor import run_stock_prediction

def detect_reversals(tickers):
    alerts = []

    for ticker in tickers:
        try:
            model, X, scaler, predicted = run_stock_prediction(ticker)
            prices = predicted.flatten()

            if len(prices) >= 3:
                if (prices[-3] > prices[-2] < prices[-1]) or (prices[-3] < prices[-2] > prices[-1]):
                    direction = "📈 Reversal Up" if prices[-1] > prices[-2] else "📉 Reversal Down"
                    alerts.append(f"{ticker}: {direction}")
        except:
            continue

    return alerts
