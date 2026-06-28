import pandas as pd

from database.db_connection import engine


def load_stock_data(ticker):

    query = f"""
        SELECT *
        FROM stock_prices
        WHERE ticker = '{ticker}'
        ORDER BY stock_date ASC
    """

    data = pd.read_sql(query, engine)

    data["stock_date"] = pd.to_datetime(
        data["stock_date"]
    )

    data.set_index("stock_date", inplace=True)

    return data