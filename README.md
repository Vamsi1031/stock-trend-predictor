# 📈 Stock Helper Pro

**Stock Helper Pro** is an advanced and beginner-friendly stock market forecasting app that uses deep learning (LSTM) to predict stock prices and provide buy/sell advice. Built with **Streamlit**, **TensorFlow**, and **yFinance**, it gives both visual and textual recommendations suitable for all levels of users.

---

## 🚀 Features

- 🔍 Predict stock trends using LSTM neural networks
- 📊 Clear matplotlib graphs showing both past & future trends
- 🧠 Intelligent buy/hold/avoid advice based on forecast
- 📊 Side-by-side stock comparison
- ⚡ Real-time alerts and market movers
- 🧒 Built with naive users in mind — no prior stock knowledge needed
- 🌙 Dark-themed professional UI using `streamlit-option-menu`

---

## 📂 Folder Structure and File Roles

```
stock-trend-predictor/
│
├── app/
│   └── main.py                  # Streamlit app frontend logic
│
├── src/                         # Core backend processing
│   ├── run_predictor.py         # LSTM model loading/training & prediction
│   ├── data_loader.py           # Fetches stock data from Yahoo Finance
│   ├── preprocessing.py         # Prepares data: scaling, shaping, windowing
│   ├── visualizer.py            # Uses matplotlib to draw forecast charts
│   └── alerts.py                # Handles real-time reversal detection
│
├── data/                        # Cached CSV data of stocks
│   └── stock_data.csv
│
├── models/                      # Trained LSTM models (.keras files saved per stock)
│   └── AAPL_model.keras
│
├── requirements.txt             # All required packages
└── README.md                    # You're reading it!
```

---

## 🔁 How It Works

### 📦 Data Pipeline:

1. **User inputs ticker** (e.g., AAPL)
2. `data_loader.py` fetches last 5 years of stock data via `yfinance`
3. `preprocessing.py` scales & reshapes the data for LSTM
4. `run_predictor.py`:
   - Loads an existing model or trains a new LSTM
   - Predicts next 30 days using sliding window
   - Returns predicted prices and original data

5. `visualizer.py`:
   - Displays the past + predicted trend in a clean matplotlib graph

6. `main.py`:
   - Generates user-friendly output including 📉 or 📈 indicators
   - Adds stock to user session, tracks predictions

---

## 🧪 How to Run Locally

### 1️⃣ Clone this repository:

```bash
git clone https://github.com/yourusername/stock-trend-predictor.git
cd stock-trend-predictor
```

### 2️⃣ Install dependencies:

```bash
pip install -r requirements.txt
```

### 3️⃣ Launch the app:

```bash
streamlit run app/main.py
```

> ⚠️ On first run, the model will train and cache for each stock.

---

## 🌐 Deploying to Streamlit Cloud

1. ✅ Push your project to GitHub
2. 🌐 Go to: [https://streamlit.io/cloud](https://streamlit.io/cloud)
3. 🔗 Sign in with GitHub and select your repo
4. 🛠 Set the entry point to: `app/main.py`
5. ✅ Deploy!

---

## 🖼 Example Output

_Replace this image with your app screenshot_

![Forecast Screenshot](https://via.placeholder.com/900x400.png?text=Stock+Forecast+Graph)

---

## 🧠 Technologies Used

| Tool             | Purpose                            |
|------------------|------------------------------------|
| `Streamlit`      | Frontend + Interactivity           |
| `yFinance`       | Real-time stock data               |
| `TensorFlow`     | LSTM modeling                      |
| `Matplotlib`     | Trend visualization                |
| `scikit-learn`   | Data preprocessing                 |

---

## 👩‍💻 Contributions

Pull requests are welcome! To contribute:

```bash
git checkout -b feature/my-feature
git commit -m "Add feature"
git push origin feature/my-feature
```

---

## 📜 License

This project is open-source under the [MIT License](LICENSE).

---

## 📬 Contact

Made with ❤️ by **Your Name**  
🔗 [GitHub](https://github.com/yourusername) | ✉️ your.email@example.com