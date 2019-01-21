import pandas as pd
import numpy as np

google_stock = pd.read_csv('GOOG.csv', index_col=['Date'], parse_dates=['Date'], usecols=['Date', 'Adj Close'])

print(google_stock.head())
