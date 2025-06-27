import numpy as np
from sklearn.preprocessing import MinMaxScaler

def preprocess_data(df, sequence_length=60):
    close_prices = df[['Close']].values
    scaler = MinMaxScaler()
    scaled_data = scaler.fit_transform(close_prices)

    X, y = [], []
    for i in range(sequence_length, len(scaled_data)):
        X.append(scaled_data[i-sequence_length:i])
        y.append(scaled_data[i])
    return np.array(X), np.array(y), scaler