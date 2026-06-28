import joblib
import numpy as np
import pandas as pd

from pipeline.process_data import process_stock_data

model = joblib.load("models/saved_models/linear_regression.pkl")


def predict_stock(ticker):

    data = process_stock_data(ticker)

    latest_row = data.iloc[-1]
      
    # model train on which  column name same should be in the database also in pipeline 
    features = pd.DataFrame([{
    "Open": latest_row["open_price"],
    "High": latest_row["high_price"],
    "Low": latest_row["low_price"],
    "Volume": latest_row["volume"],
    "MA_10": latest_row["MA_10"],
    "MA_50": latest_row["MA_50"],
    "Return": latest_row["Return"],
    "Volatility": latest_row["Volatility"]
}])

    predicted_close = model.predict(features)[0]

    latest_close = latest_row["close_price"]

    if predicted_close > latest_close:
        direction = "UP"
    else:
        direction = "DOWN"

    predicted_volatility = latest_row["Volatility"]

    predicted_change_percent = (
        (predicted_close - latest_close)
        / latest_close
    ) * 100

    return {
        "ticker": ticker,
        "latest_close": latest_close,
        "predicted_close": predicted_close,
        "direction": direction,
        "volatility": predicted_volatility,
        "predicted_change_percent": predicted_change_percent
    }