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

# Create a DataFrame with only Bob's data
bob_shopping_carts = pd.DataFrame(items, columns=['Bob'])

# Show bob_shopping_carts
print(bob_shopping_carts)

# Create a DataFrame with only some items from Alice and Bob
sel_shopping_carts = pd.DataFrame(items, index=['pants', 'book'])

# Show sel_shopping_carts
print(sel_shopping_carts)

# Create a DataFrame with some items form Alice
alice_sel_shopping_carts = pd.DataFrame(items, index=['glasses', 'bike'], columns=['Alice'])

# Show alice sel shopping_carts
print(alice_sel_shopping_carts)

# Create a DataFrame from arrays dictionary
# Important: all the list had to have the same size

# Create a array dictionary
data = {'Integer': [1, 2, 4],
        'Floats': [4.5, 8.2, 9.6]}

# Create a DataFrame
df = pd.DataFrame(data)

# Show the DataFrame
print(df)

# add a index for DataFrame df
df = pd.DataFrame(data, index=['label 1', 'label 2', 'label 3'])

# show again the data with labels
print(df)

# Create a DataFrame from dictionaries
items2 = [{'bikes': 20, 'pants': 30, 'watches': 35},
        {'watches': 10, 'glasses': 50, 'bikes': 15, 'pants': 5}]

# Create a DataFrame
store_items = pd.DataFrame(items2)

# Show the DataFrame
print(store_items)

# Add a index to DataFrame store_items
store_items = pd.DataFrame(items2, index=['store 1', 'store 2'])

# Show the new DataFrame
print(store_items)
