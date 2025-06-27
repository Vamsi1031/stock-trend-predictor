import numpy as np

def analyze_trend(predicted_prices):
    # Basic logic: last 3 days trend
    changes = np.diff(predicted_prices[-4:])
    avg_change = np.mean(changes)

    if avg_change > 1.5:
        return "📈 **Recommendation: Buy** — strong upward trend detected."
    elif avg_change < -1.5:
        return "📉 **Recommendation: Sell** — downward trend likely."
    else:
        return "⚖️ **Recommendation: Hold** — market is stable."

def volatility_index(prices):
    return np.std(prices[-30:])  # Simple recent volatility check
