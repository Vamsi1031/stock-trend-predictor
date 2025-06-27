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



## 🖼 Example Output
![Screenshot (3)](https://github.com/user-attachments/assets/3a6753fd-296f-4d96-89d2-4336a8438cd9)

![Screenshot (4)](https://github.com/user-attachments/assets/4232e4e0-9493-458e-a04f-8cda4cf5113a)

![Screenshot (5)](https://github.com/user-attachments/assets/7375ed90-356f-4d9d-a0e4-c1902bf22c12)

![Screenshot (6)](https://github.com/user-attachments/assets/168bb2c5-c401-4c20-8f43-ce20e2dfc2a4)

![Screenshot (7)](https://github.com/user-attachments/assets/35d36181-394d-4ce7-870b-a519fe0aca23)





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

Made with ❤️ by **KOLUSU VAMSI KRISHNA**  
🔗 [GitHub](https://github.com/Vamsikolusu1031) | ✉️ kolusuvamsi9@gmail.com
