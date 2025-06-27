import matplotlib.pyplot as plt
import numpy as np
import io
from PIL import Image

def plot_prediction_graph(past_data, predicted_data, title="Stock Price Forecast"):
    predicted_data = predicted_data.flatten() if hasattr(predicted_data, 'flatten') else predicted_data

    if past_data is not None:
        past_data = past_data.flatten() if hasattr(past_data, 'flatten') else past_data
        x_past = np.arange(len(past_data))
        x_future = np.arange(len(past_data), len(past_data) + len(predicted_data))
    else:
        past_data = []
        x_past = []
        x_future = np.arange(len(predicted_data))

    fig, ax = plt.subplots(figsize=(10, 5), facecolor="#0E1117")
    ax.set_facecolor("#0E1117")

    if len(past_data):
        ax.plot(x_past, past_data, color='skyblue', label='Past Prices', linewidth=2)

    ax.plot(x_future, predicted_data, color='limegreen', linestyle='--', label='Predicted', linewidth=2)

    ax.set_title(title, color="white", fontsize=14)
    ax.set_xlabel("Days", color="white")
    ax.set_ylabel("Price", color="white")
    ax.tick_params(colors="white")
    ax.legend(facecolor="#0E1117", edgecolor="white", labelcolor="white")

    for spine in ax.spines.values():
        spine.set_color("white")

    ax.grid(True, color="gray", linestyle="--", linewidth=0.3)

    buf = io.BytesIO()
    plt.tight_layout()
    plt.savefig(buf, format="png", facecolor=fig.get_facecolor())
    buf.seek(0)
    img = Image.open(buf)
    plt.close()
    return img
