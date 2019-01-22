import pandas as pd
import numpy as np

# Load the Google stock data
google_stock = pd.read_csv('GOOG.csv', index_col=['Date'], parse_dates=['Date'], usecols=['Date', 'Adj Close'])

# Load the Apple stock data
apple_stock = pd.read_csv('AAPL.csv', index_col=['Date'], parse_dates=['Date'], usecols=['Date', 'Adj Close'])

# Load the Amazon stock data
amazon_stock = pd.read_csv('AMZN.csv', index_col=['Date'], parse_dates=['Date'], usecols=['Date', 'Adj Close'])

# Display the Google DataFrame
print(google_stock.head())

# Create calendar dates between '2000-01-01' and  '2016-12-31'
dates = pd.date_range('2000-01-01', '2016-12-31')

# Create and empty DataFrame that uses the above dates as indices
all_stocks = pd.DataFrame(index=dates)

# Change the Adj Close column label to Google
google_stock = google_stock.rename(index=str, columns={'Adj Close': 'Google Adj Close'})
print(google_stock.head())

# Change the Adj Close column label to Apple
#apple_stock =

# Change the Adj Close column label to Amazon
#amazon_stock =
