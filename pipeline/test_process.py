from pipeline.load_data import load_stock_data

data = load_stock_data("AAPL")

print(data.head())

print(data.columns)