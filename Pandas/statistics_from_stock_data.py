import pandas as pd
import matplotlib.pyplot as plt


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
google_stock = google_stock.rename(index=str, columns={'Adj Close': 'Google'})
print(google_stock.head())

# Change the Adj Close column label to Apple
apple_stock = apple_stock.rename(index=str, columns={'Adj Close': 'Apple'})
print(apple_stock.head())

# Change the Adj Close column label to Amazon
amazon_stock = amazon_stock.rename(index=str, columns={'Adj Close': 'Amazon'})
print(amazon_stock.head())

# Join the Google stock to all_stocks
all_stocks = all_stocks.join(google_stock)

# Join the Apple stock to all_stocks
all_stocks = all_stocks.join(apple_stock)

# Join the Amazon stock to all_stocks
all_stocks = all_stocks.join(amazon_stock)

print(all_stocks.head())
print(all_stocks.tail())

# Check if there are any NaN values in the all_stocks DataFrame
print(all_stocks.isnull().any())

# Remove any rows that contain NaN values
all_stocks.dropna(inplace=True)
print(all_stocks.isnull().any())

# Print the average stock price for each stock
print('The average stock prices for each stock:\n', all_stocks.mean())

# Print the median stock price for each stock
print('The median stock price for each stock:\n', all_stocks.median())

# Print the standard deviation of the stock price for each stock
print('The standard deviation of the stock price for each stock:\n', all_stocks.std())

# Print the correlation between stocks
print('The correlation between stocks: \n', all_stocks.corr())

# We compute the rolling mean using a 150-Day window for Google stock
rollingMean = google_stock.rolling(150).mean()
print(rollingMean)

# We plot the Google stock data
plt.plot(all_stocks['Google'])

# We plot the rolling mean ontop of our Google stock data
plt.plot(rollingMean)
plt.legend(['Google Stock Price', 'Rolling Mean'])
plt.show()
