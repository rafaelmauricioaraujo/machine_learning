# importing pandas
import pandas as pd

# Create a dictionary
items = {'Bob': pd.Series(data=[245, 25, 55], index=['bike', 'pants', 'watch']),
         'Alice': pd.Series(data=[40, 110, 500, 45], index=['book', 'glasses', 'bike', 'pants'])}

# show the type to confirm that is a dictionary
print(type(items))

# Create a Pandas DataFrame, using as parameter the dictionary
shopping_carts = pd.DataFrame(items)
print(shopping_carts)

# Create a Pandas Series Dictionary without index
data = {'Bob': pd.Series([245, 25, 55]),
        'Alice': pd.Series([40, 110, 500, 45])}

# Create a DataFrame
df = pd.DataFrame(data)

# Showing the DataFrame
print(df)

# Is also to get some information about shopping carts
print('shopping_carts.shape: ', shopping_carts.shape)
print('shopping_carts dimension: ', shopping_carts.ndim)
print('shopping_carts have a amount of: ', shopping_carts.size, 'elements')
print()
print('shopping_carts data: ', shopping_carts.values)
print()
print('shopping_carts index: ', shopping_carts.index)
print()
print('shopping_carts columns: ', shopping_carts.columns)
