import pandas as pd

from database.db_connection import engine


def process_stock_data(ticker):

    query = f"""
        SELECT *
        FROM stock_prices
        WHERE ticker = '{ticker}'
        ORDER BY stock_date ASC
    """

    data = pd.read_sql(query, engine)

    # useful features 

    data["MA_10"] = data["close_price"].rolling(window=10).mean()

    data["MA_50"] = data["close_price"].rolling(window=50).mean()

    data["Return"] = data["close_price"].pct_change()

    data["Volatility"] = data["Return"].rolling(window=10).std()

    data.dropna(inplace=True)

    return data