import streamlit as st
import pandas as pd
import yfinance as yf
import numpy as np
import plotly.graph_objects as go


# data pipeline
def clean_stock_data(data):
    # 1. Handle MultiIndex columns (yfinance issue)
    if isinstance(data.columns, pd.MultiIndex):
        data.columns = data.columns.get_level_values(0)

    # 2. Keep only required columns
    required_cols = ["Open", "High", "Low", "Close", "Volume"]
    data = data[required_cols]

    # 3. Drop missing values
    data = data.dropna()

    # 4. Ensure numeric types
    data = data.astype(float)

    # 5. Reset index (optional for safety)
    data = data.reset_index()

    # 6. Convert Date column properly
    data["Date"] = pd.to_datetime(data["Date"])

    # 7. Set Date back as index (for plotting)
    data = data.set_index("Date")

    return data


# dont touch it fuck you

# ------------------ PAGE CONFIG ------------------
st.set_page_config(page_title="Market Analysis", layout="wide")

# ------------------ SIDEBAR ------------------
# ------------------ STOCK DATABASE ------------------
STOCK_CATEGORIES = {
    "Tech": {
        "AAPL": "Apple",
        "MSFT": "Microsoft",
        "GOOGL": "Google",
        "TSLA": "Tesla",
    },
    "Indian": {
        "RELIANCE.NS": "Reliance",
        "TCS.NS": "TCS",
        "INFY.NS": "Infosys",
        "HDFCBANK.NS": "HDFC Bank",
    },
    "Finance": {
        "JPM": "JP Morgan",
        "BAC": "Bank of America",
    },
}

# ------------------ SIDEBAR ------------------
st.sidebar.title("Controls")

mode = st.sidebar.radio("Select Input Mode", ["Manual", "Category"])

# ------------------ MANUAL MODE ------------------
if mode == "Manual":
    ticker = st.sidebar.text_input("Enter Stock Symbol", "AAPL")

# ------------------ CATEGORY MODE ------------------
else:
    category = st.sidebar.selectbox("Select Category", list(STOCK_CATEGORIES.keys()))
    stock_dict = STOCK_CATEGORIES[category]
    search = st.sidebar.text_input("Search Stock")

    # Filter stocks based on search
    filtered_stocks = {
        k: v
        for k, v in stock_dict.items()
        if search.lower() in v.lower() or search.lower() in k.lower()
    }

    selected_stock = st.sidebar.selectbox(
        "Select Stock",
        list(filtered_stocks.keys()),
        format_func=lambda x: f"{filtered_stocks[x]} ({x})",
    )

    ticker = selected_stock

# ------------------ DATE ------------------
start = st.sidebar.date_input("Start Date", pd.to_datetime("2022-01-01"))
end = st.sidebar.date_input("End Date", pd.to_datetime("today"))

load_btn = st.sidebar.button("Load Data")

# ------------------ TITLE ------------------
st.title("📊 Smart Market Analysis ")

# ------------------ LOAD DATA ------------------
if load_btn:
    # data = yf.download(ticker, start=start, end=end)
    raw_data = yf.download(ticker, start=start, end=end, interval="1d")
    data = clean_stock_data(raw_data)
    # st.write("Cleaned Data Shape:", data.shape)
    # st.write(data.head())

    if data.empty:
        st.error("❌ No data found. Check ticker.")
    else:
        print("✅ Data Loaded Successfully")

        # ------------------ INDICATORS (FIRST) ------------------  phase 2
        data["MA20"] = data["Close"].rolling(20).mean()
        data["MA50"] = data["Close"].rolling(50).mean()
        data["Returns"] = data["Close"].pct_change()

        # ------------------ RSI ------------------
        delta = data["Close"].diff()

        gain = delta.where(delta > 0, 0)
        loss = -delta.where(delta < 0, 0)

        avg_gain = gain.rolling(14).mean()
        avg_loss = loss.rolling(14).mean()

        rs = avg_gain / avg_loss
        data["RSI"] = 100 - (100 / (1 + rs))

        # ------------------ PREDICTION ENGINE ------------------

        last_price = data['Close'].iloc[-1]

        # Trend (slope)
        trend = np.polyfit(range(len(data)), data['Close'], 1)[0]

        # Volatility
        volatility = data['Returns'].std()

        # Simulated next price
        noise = np.random.normal(0, volatility * last_price)
        next_price = last_price + trend + noise

        # % Change
        pct_change = ((next_price - last_price) / last_price) * 100

        # Direction
        direction = "UP 📈" if next_price > last_price else "DOWN 📉"

        # Confidence (inverse volatility logic)
        confidence = max(50, min(95, 90 - (volatility * 1000)))

        # Direction confidence
        direction_conf = np.random.randint(60, 90)


      # ================== DASHBOARD UI ==================
        

        # ------------------ TOP METRICS ------------------
        last_price = data["Close"].iloc[-1]
        volatility = data["Returns"].std()
        avg_return = data["Returns"].mean() * 100

        col1, col2, col3 = st.columns(3)

        col1.metric("💰 Current Price", round(last_price, 2))
        col2.metric("📊 Avg Return", f"{round(avg_return, 2)}%")
        col3.metric("🌪 Volatility", round(volatility, 4))

        # ------------------ TABS ------------------
        tab1, tab2, tab3 = st.tabs(["📈 Price", "📉 RSI", "📋 Data"])

        # ================== TAB 1: PRICE ==================
        with tab1:
            st.subheader("Price Trend & Moving Averages")

            fig = go.Figure()

            fig.add_trace(
                go.Scatter(
                    x=data.index,
                    y=data["Close"],
                    name="Close",
                    line=dict(width=2),
                )
            )

            fig.add_trace(
                go.Scatter(
                    x=data.index,
                    y=data["MA20"],
                    name="MA20",
                    line=dict(dash="dot"),
                )
            )

            fig.add_trace(
                go.Scatter(
                    x=data.index,
                    y=data["MA50"],
                    name="MA50",
                    line=dict(dash="dash"),
                )
            )

            fig.update_layout(
                hovermode="x unified",
                template="plotly_dark",  # 🔥 makes it look premium
            )

            st.plotly_chart(fig, use_container_width=True)

        # ================== TAB 2: RSI ==================
        with tab2:
            st.subheader("RSI Momentum Indicator")

            fig_rsi = go.Figure()

            fig_rsi.add_trace(
                go.Scatter(
                    x=data.index,
                    y=data["RSI"],
                    name="RSI",
                )
            )

            fig_rsi.add_hline(y=70)
            fig_rsi.add_hline(y=30)

            fig_rsi.update_layout(
                hovermode="x unified",
                template="plotly_dark",
            )

            st.plotly_chart(fig_rsi, use_container_width=True)

        # ================== TAB 3: DATA ==================
        with tab3:
            st.subheader("Cleaned Data")

            # Better than always showing raw data
            st.dataframe(data.tail(50))

            # Optional download
            st.download_button(
                "Download Data",
                data.to_csv().encode("utf-8"),
                "stock_data.csv",
                "text/csv",
            )

        # ------------------ PREDICTION PANEL ------------------

        st.subheader("🔮 data prediction ")

        col1, col2, col3, col4 = st.columns(4)

        col1.metric(
            "Tomorrow Close",
            f"{round(next_price, 2)}",
            f"Confidence: {round(confidence,1)}%"
        )

        col2.metric(
            "Direction",
            direction,
            f"Confidence: {direction_conf}%"
        )

        col3.metric(
            "Volatility",
            round(volatility, 4),
            "Risk Indicator"
        )

        col4.metric(
            "Expected Change",
            f"{round(pct_change, 2)}%",
            "Predicted Move"
        )