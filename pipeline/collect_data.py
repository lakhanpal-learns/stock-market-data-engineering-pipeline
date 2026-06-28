import yfinance as yf
import pandas as pd

from sqlalchemy import text
from database.db_connection import engine


def collect_stock_data(ticker, start_date, end_date):

    # DOWNLOAD DATA
    data = yf.download(
        ticker,
        start=start_date,
        end=end_date
    )

    # CHECK EMPTY
    if data.empty:
        return None

    # FLATTEN MULTI-INDEX
    if isinstance(data.columns, pd.MultiIndex):
     data.columns = data.columns.droplevel(1)

    # RESET INDEX
    data.reset_index(inplace=True)

    # RENAME COLUMNS
    data.rename(columns={
        "Date": "stock_date",
        "Open": "open_price",
        "High": "high_price",
        "Low": "low_price",
        "Close": "close_price",
        "Volume": "volume"
    }, inplace=True)

    # ADD TICKER
    data["ticker"] = ticker

    # FINAL COLUMNS
    data = data[
        [
            "ticker",
            "stock_date",
            "open_price",
            "high_price",
            "low_price",
            "close_price",
            "volume"
        ]
    ]

    # DATABASE OPERATIONS
    with engine.begin() as connection:

        # CHECK EXISTING TICKERS
        result = connection.execute(
            text("SELECT DISTINCT ticker FROM stock_prices")
        )

        existing_tickers = [row[0] for row in result]

        # DELETE OLD COMPANY DATA
        if existing_tickers and ticker not in existing_tickers:

            connection.execute(
                text("DELETE FROM stock_prices")
            )

            print("Old company data removed.")

        # UPSERT LOGIC
        for _, row in data.iterrows():

            query = text("""

                INSERT INTO stock_prices (
                    ticker,
                    stock_date,
                    open_price,
                    high_price,
                    low_price,
                    close_price,
                    volume
                )

                VALUES (
                    :ticker,
                    :stock_date,
                    :open_price,
                    :high_price,
                    :low_price,
                    :close_price,
                    :volume
                )

                ON CONFLICT (ticker, stock_date)
                DO NOTHING;

            """)

            connection.execute(query, {
                "ticker": row["ticker"],
                "stock_date": row["stock_date"],
                "open_price": row["open_price"],
                "high_price": row["high_price"],
                "low_price": row["low_price"],
                "close_price": row["close_price"],
                "volume": row["volume"]
            })

    print("Stock data stored successfully!")

    return data