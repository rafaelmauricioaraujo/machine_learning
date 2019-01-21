import pandas as pd
import numpy as np

# Load the Google stock data
google_stock = pd.read_csv('GOOG.csv', index_col=['Date'], parse_dates=['Date'], usecols=['Date', 'Adj Close'])

# Load the Apple stock data
apple_stock = pd.read_csv('AAPL.csv', index_col=['Date'], parse_dates=['Date'], usecols=['Date', 'Adj Close'])

# Load the Amazon stock data

amazon_stock = pd.read_csv('AMZN.csv', index_col=['Date'], parse_dates=['Date'], usecols=['Date', 'Adj Close'])

print(google_stock.head())
