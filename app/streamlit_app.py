import streamlit as st
import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), '..')
    )
)
from pipeline.collect_data import load_stock_data

ticker = st.text_input("Enter Ticker", "AAPL")
ticker = ticker.upper().strip()

start_date = st.date_input("Start Date")

end_date = st.date_input("End Date")

if st.button("Load Stock Data"):

    if start_date >= end_date:
        st.error("End date must be after start date.")

    else:

        df = load_stock_data(
            ticker,
            start_date,
            end_date
        )

        if df is not None:

            st.success("Data loaded successfully!")

            st.dataframe(df.head())

        else:
            st.error("Invalid ticker or no data found.")

