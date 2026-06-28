import streamlit as st
import pandas as pd
import plotly.graph_objects as go

from pipeline.collect_data import collect_stock_data

from pipeline.load_data import load_stock_data

from pipeline.process_data import process_stock_data

from pipeline.predict import predict_stock

from pipeline.save_prediction import save_prediction


# ------------------ PAGE CONFIG ------------------
st.set_page_config(
    page_title="Smart Market Analysis",
    layout="wide"
)


# ------------------ STOCK DATABASE ------------------
STOCK_CATEGORIES = {
    "Tech": {
        "AAPL": "Apple",
        "MSFT": "Microsoft",
        "GOOGL": "Google",
        "TSLA": "Tesla",
        "NVDA": "NVIDIA",
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

mode = st.sidebar.radio(
    "Select Input Mode",
    ["Manual", "Category"]
)


# ------------------ MANUAL MODE ------------------
if mode == "Manual":

    ticker = st.sidebar.text_input(
        "Enter Stock Symbol",
        "AAPL"
    ).upper()


# ------------------ CATEGORY MODE ------------------
else:

    category = st.sidebar.selectbox(
        "Select Category",
        list(STOCK_CATEGORIES.keys())
    )

    stock_dict = STOCK_CATEGORIES[category]

    search = st.sidebar.text_input("Search Stock")

    filtered_stocks = {
        k: v
        for k, v in stock_dict.items()
        if search.lower() in v.lower()
        or search.lower() in k.lower()
    }

    selected_stock = st.sidebar.selectbox(
        "Select Stock",
        list(filtered_stocks.keys()),
        format_func=lambda x:
        f"{filtered_stocks[x]} ({x})"
    )

    ticker = selected_stock


# ------------------ DATE INPUTS ------------------
start = st.sidebar.date_input(
    "Start Date",
    pd.to_datetime("2019-01-01")
)

end = st.sidebar.date_input(
    "End Date",
    pd.to_datetime("today")
)


# ------------------ LOAD BUTTON ------------------
load_btn = st.sidebar.button("Load Data")


# ------------------ TITLE ------------------
st.title("📊 Smart Market Analysis")


# ==================================================
# MAIN PIPELINE
# ==================================================

if load_btn:

    try:

        # ==========================================
        # RUN ETL PIPELINE
        # ==========================================

        collect_stock_data(
            ticker=ticker,
            start_date=start,
            end_date=end
        )


        # ==========================================
        # LOAD DATA FROM POSTGRESQL
        # ==========================================

        data = load_stock_data(ticker)


        # ==========================================
        # CHECK EMPTY DATA
        # ==========================================

        if data.empty:
            st.error("❌ No data found")

        else:

            # ======================================
            # FEATURE ENGINEERING
            # ======================================

            data["MA20"] = (
                data["close_price"]
                .rolling(20)
                .mean()
            )

            data["MA50"] = (
                data["close_price"]
                .rolling(50)
                .mean()
            )

            data["Returns"] = (
                data["close_price"]
                .pct_change()
            )


            # ======================================
            # RSI
            # ======================================

            delta = data["close_price"].diff()

            gain = delta.where(delta > 0, 0)
            loss = -delta.where(delta < 0, 0)

            avg_gain = gain.rolling(14).mean()
            avg_loss = loss.rolling(14).mean()

            rs = avg_gain / avg_loss

            data["RSI"] = 100 - (100 / (1 + rs))


            # ======================================
            # PREDICTION PIPELINE
            # ======================================

            prediction_result = predict_stock(ticker)

            save_prediction(prediction_result)


            # ======================================
            # METRICS
            # ======================================

            last_price = float(
                data["close_price"].iloc[-1]
            )

            volatility = float(
                data["Returns"].std()
            )

            avg_return = float(
                data["Returns"].mean() * 100
            )


            col1, col2, col3 = st.columns(3)

            col1.metric(
                "💰 Current Price",
                round(last_price, 2)
            )

            col2.metric(
                "📊 Avg Return",
                f"{round(avg_return, 2)}%"
            )

            col3.metric(
                "🌪 Volatility",
                round(volatility, 4)
            )


            # ======================================
            # TABS
            # ======================================

            tab1, tab2, tab3 = st.tabs([
                "📈 Price",
                "📉 RSI",
                "📋 Data"
            ])


            # ======================================
            # TAB 1 : PRICE
            # ======================================

            with tab1:

                st.subheader(
                    "Price Trend & Moving Averages"
                )

                fig = go.Figure()

                fig.add_trace(
                    go.Scatter(
                        x=data.index,
                        y=data["close_price"],
                        name="Close Price",
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
                    template="plotly_dark",
                    height=600
                )

                st.plotly_chart(
                    fig,
                    use_container_width=True
                )


            # ======================================
            # TAB 2 : RSI
            # ======================================

            with tab2:

                st.subheader(
                    "RSI Momentum Indicator"
                )

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
                    height=500
                )

                st.plotly_chart(
                    fig_rsi,
                    use_container_width=True
                )


            # ======================================
            # TAB 3 : DATA
            # ======================================

            with tab3:

                st.subheader("Database Stock Data")

                st.dataframe(data.tail(50))

                st.download_button(
                    "Download Data",
                    data.to_csv().encode("utf-8"),
                    "stock_data.csv",
                    "text/csv",
                )

            
            # ======================================
            # PREDICTION PANEL
            # ======================================

            st.subheader("🔮 Forcasting  Panel")

            pcol1, pcol2, pcol3, pcol4 = st.columns(4)

            pcol1.metric(
                "Tomorrow Close",
                f"{round(prediction_result['predicted_close'], 2)}"
            )

            pcol2.metric(
                "Direction",
                prediction_result["direction"]
            )

            pcol3.metric(
                "Volatility",
                round(prediction_result["volatility"], 4)
            )

            pcol4.metric(
                "Expected Change",
                f"{round(prediction_result['predicted_change_percent'], 2)}%"
            )
            
            # ======================================
            # HISTORICAL PREDICTIONS PANEL
            # ======================================

            st.subheader("📜 Historical Predictions")

            with st.expander("View Historical Predictions"):

                from sqlalchemy import text
                from database.db_connection import engine

                history_query = text("""
                    SELECT
                        ticker,
                        prediction_date,
                        latest_close,
                        predicted_close,
                        predicted_direction,
                        predicted_volatility,
                        predicted_change_percent,
                        model_version,
                        created_at
                    FROM predictions
                    WHERE ticker = :ticker
                    ORDER BY created_at DESC
                """)

                history_df = pd.read_sql(
                    history_query,
                    engine,
                    params={"ticker": ticker}
                )

                if history_df.empty:

                    st.warning("No historical predictions found")

                else:

                    # FILTERS
                    filter_col1, filter_col2 = st.columns(2)

                    with filter_col1:

                        direction_filter = st.selectbox(
                            "Filter Direction",
                            ["ALL", "UP", "DOWN"]
                        )

                    with filter_col2:

                        row_limit = st.slider(
                            "Rows to Display",
                            min_value=5,
                            max_value=100,
                            value=10,
                            step=5
                        )

                    # APPLY FILTER
                    if direction_filter != "ALL":

                        history_df = history_df[
                            history_df["predicted_direction"]
                            == direction_filter
                        ]

                    # LIMIT ROWS
                    history_df = history_df.head(row_limit)

                    st.dataframe(
                        history_df,
                        use_container_width=True
                    )

                    # DOWNLOAD BUTTON
                    st.download_button(
                        "Download Prediction History",
                        history_df.to_csv(index=False).encode("utf-8"),
                        "prediction_history.csv",
                        "text/csv"
                    )

                # ======================================
                # SUCCESS MESSAGE
                # ======================================

                st.success(
                    "✅ Pipeline executed successfully"
                )


    except Exception as e:

        st.error(f"❌ Error: {e}")


