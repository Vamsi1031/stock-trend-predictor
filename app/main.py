import streamlit as st
from streamlit_option_menu import option_menu
from src.run_predictor import run_stock_prediction
from src.alerts import detect_reversals

# ✅ Must be first
st.set_page_config(page_title="Stock Helper Pro", layout="wide")

# ✅ Track user searched stocks
if "user_stocks" not in st.session_state:
    st.session_state.user_stocks = set()

# ✅ Navigation bar
selected = option_menu(
    menu_title=None,
   options=["Home", "Predict", "Compare", "Top 5", "About"],
icons=["house", "graph-up-arrow", "columns-gap", "trophy", "info-circle"],

    orientation="horizontal",
    default_index=0,
    styles={
        "container": {"padding": "0!important", "background-color": "#0E1117"},
        "icon": {"color": "white", "font-size": "20px"},
        "nav-link": {"color": "white", "font-size": "16px", "text-align": "center", "margin": "0px"},
        "nav-link-selected": {"background-color": "#6c63ff"},
    }
)

# ✅ HOME PAGE
if selected == "Home":
    st.title("🏠 Welcome to Stock Helper Pro")
    st.markdown("Predict, compare, and get clear advice — all in one simple tool 💹")

    # 🔔 Show daily alerts as a notice box
    from src.alerts import detect_reversals
    tickers_to_check = ["AAPL", "TSLA", "MSFT", "GOOGL", "AMZN", "RELIANCE.NS", "TCS.NS", "HDFCBANK.NS"]

    with st.expander("🔔 Today's Trend Alerts", expanded=True):
        alerts = detect_reversals(tickers_to_check)

        if alerts:
            alert_text = " | ".join(alerts)
            st.markdown(
                f"<marquee behavior='scroll' direction='left' scrollamount='5' style='color:orange; font-size:18px;'>⚠️ {alert_text}</marquee>",
                unsafe_allow_html=True
            )
        else:
            st.success("✅ No major reversals detected today.")


    # ✅ Optional: Show user stocks
    with st.expander("🧠 Stocks you've searched this session"):
        st.write(", ".join(st.session_state.user_stocks) or "None yet.")

# ✅ PREDICT PAGE
elif selected == "Predict":
    st.title("📈 Predict Single Stock")

    if "predicted_prices" not in st.session_state:
        st.session_state.predicted_prices = None
        st.session_state.model = None
        st.session_state.ticker = "AAPL"

    st.markdown("### 📘 Choose a stock (or type your own):")

    # Dropdown for naive users
    popular_stocks = ["AAPL", "TSLA", "MSFT", "RELIANCE.NS", "TCS.NS", "INFY.NS"]
    dropdown_choice = st.selectbox("🔽 Popular Stocks:", popular_stocks)
    ticker = dropdown_choice

    if st.button("🚀 Predict and Advise"):
        model, X, scaler, predicted_prices = run_stock_prediction(ticker)

        if model:
            st.session_state.predicted_prices = predicted_prices
            st.session_state.model = model
            st.session_state.ticker = ticker
            st.session_state.user_stocks.add(ticker)

            st.line_chart(predicted_prices[-30:].flatten())
            trend = "📈 Rising" if predicted_prices[-1] > predicted_prices[-2] else "📉 Falling"
            suggestion = "✅ Buy" if trend == "📈 Rising" else "⚠️ Hold or Avoid"
            st.metric(label="Trend", value=trend)
            st.metric(label="Advice", value=suggestion)
        else:
            st.error("⚠️ Failed to generate prediction.")

# ✅ COMPARE PAGE
elif selected == "Compare":
    st.title("📊 Compare Multiple Stocks")

    # User custom input
    custom_ticker = st.text_input("✏️ Enter any stock ticker (e.g., NFLX, AMZN, HDFCBANK.NS):")
    dropdown_choice = "AAPL"  # fallback
    ticker = custom_ticker.strip().upper() if custom_ticker else dropdown_choice
    if ticker:
        st.session_state.user_stocks.add(ticker)

    if st.button("🚀 Predict and Advise"):
        model, X, scaler, predicted_prices = run_stock_prediction(ticker)

        if model:
            st.session_state.predicted_prices = predicted_prices
            st.session_state.model = model
            st.session_state.ticker = ticker
            st.session_state.user_stocks.add(ticker)

            st.line_chart(predicted_prices[-30:].flatten())
            trend = "📈 Rising" if predicted_prices[-1] > predicted_prices[-2] else "📉 Falling"
            suggestion = "✅ Buy" if trend == "📈 Rising" else "⚠️ Hold or Avoid"
            st.metric(label="Trend", value=trend)
            st.metric(label="Advice", value=suggestion)
        else:
            st.error("⚠️ Failed to generate prediction.")

    st.markdown("---")
    st.subheader("📊 Compare Multiple Stocks Side-by-Side")

    ticker_inputs = st.text_input("Enter up to 3 stock tickers (comma-separated):", "AAPL, TSLA, TCS.NS")

    if st.button("🔍 Compare Selected Stocks"):
        tickers = [t.strip().upper() for t in ticker_inputs.split(",") if t.strip()]

        if not tickers:
            st.warning("❗ Please enter at least one valid stock ticker.")
        else:
            tickers = tickers[:3]
            columns = st.columns(len(tickers))

            for i, ticker in enumerate(tickers):
                st.session_state.user_stocks.add(ticker)
                with columns[i]:
                    st.markdown(f"### {ticker}")
                    model, X, scaler, predicted_prices = run_stock_prediction(ticker)

                    if model and predicted_prices is not None:
                        trend = "📈 Rising" if predicted_prices[-1] > predicted_prices[-2] else "📉 Falling"
                        suggestion = "✅ Buy" if trend == "📈 Rising" else "⚠️ Hold or Avoid"

                        st.metric(label="Trend", value=trend)
                        st.metric(label="Advice", value=suggestion)
                        st.line_chart(predicted_prices[-30:].flatten())
                    else:
                        st.error("❌ Unable to predict.")

elif selected == "Top 5":
    st.title("🏆 Top 5 Stocks to Watch Today")

    with st.spinner("Analyzing popular stocks..."):
        from src.top_stocks import get_top_stocks
        popular_stocks = ["AAPL", "TSLA", "MSFT", "GOOGL", "META", "AMZN", "INFY.NS", "RELIANCE.NS", "TCS.NS", "HDFCBANK.NS"]
        top_stocks = get_top_stocks(popular_stocks)

    if not top_stocks:
        st.warning("Could not find strong recommendations today.")
    else:
        cols = st.columns(len(top_stocks))
        for i, stock in enumerate(top_stocks):
            with cols[i]:
                st.subheader(stock["ticker"])
                st.metric(label="Trend", value="📈 Up" if stock["trend_value"] > 0 else "📉 Down")
                st.metric(label="Advice", value=stock["suggestion"])
                st.line_chart(stock["predicted_prices"])


# ✅ ABOUT PAGE
elif selected == "About":
    st.title("ℹ️ About This App")
    st.markdown("""
        - Built for all levels of users 👶👩‍💻  
        - Uses LSTM for predictions  
        - Suggests based on trend analysis  
        - Developed with ❤️ using Python + Streamlit  
    """)
