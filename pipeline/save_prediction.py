import pandas as pd
from datetime import date
from sqlalchemy import text

from database.db_connection import engine

# problem :- recursive function conflict
# -----------------------------------
# Check if prediction already exists
# -----------------------------------

def prediction_exists(ticker):

    query = text("""
        SELECT COUNT(*)
        FROM predictions
        WHERE ticker = :ticker
        AND prediction_date = CURRENT_DATE
    """)

    with engine.connect() as conn:

        result = conn.execute(
            query,
            {"ticker": ticker}
        ).scalar()

    return result > 0


# -----------------------------------
# Save prediction
# -----------------------------------

def save_prediction(prediction_result):

    # CACHE CHECK
    if prediction_exists(prediction_result["ticker"]):

        print("Prediction already exists for today!")

        return

    # CREATE DATAFRAME
    prediction_df = pd.DataFrame([{
        "ticker": prediction_result["ticker"],

        "prediction_date": date.today(),

        "latest_close": prediction_result["latest_close"],

        "predicted_close": prediction_result["predicted_close"],

        "predicted_direction": prediction_result["direction"],

        "predicted_volatility": prediction_result["volatility"],

        "predicted_change_percent":
            prediction_result["predicted_change_percent"],

        "model_version": "linear_regression_v1"
    }])

    # SAVE TO POSTGRESQL
    prediction_df.to_sql(
        "predictions",
        engine,
        if_exists="append",
        index=False
    )

    print("Prediction saved successfully!")