# importing pandas
import pandas as pd
import numpy as np

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

# Exercise
# Since we will be working with ratings, we will set the precision of our
# dDtaFrame to one decimal place.
pd.set_option('precision', 1)

# Create a Pandas DataFrame that contains the ratings some users have given to a
# series of books. The ratings given are in the range from 1 to 5, with 5 being
# the best score. The names of the books, the authors, and the ratings of each user
# are given below:

books = pd.Series(data=['Great Expectations', 'Of Mice and Men', 'Romeo and Juliet', 'The Time Machine', 'Alice in Wonderland' ])
authors = pd.Series(data=['Charles Dickens', 'John Steinbeck', 'William Shakespeare', ' H. G. Wells', 'Lewis Carroll' ])

user_1 = pd.Series(data=[3.2, np.nan, 2.5])
user_2 = pd.Series(data=[5., 1.3, 4.0, 3.8])
user_3 = pd.Series(data=[2.0, 2.3, np.nan, 4])
user_4 = pd.Series(data=[4, 3.5, 4, 5, 4.2])

# Users that have np.nan values means that the user has not yet rated that book.
# Use the data above to create a Pandas DataFrame that has the following column
# labels: 'Author', 'Book Title', 'User 1', 'User 2', 'User 3', 'User 4'. Let Pandas
# automatically assign numerical row indices to the DataFrame.

# Create a dictionary with the data given above
dat = {'Author': authors,
       'Book Title': books,
       'User 1': user_1,
       'User 2': user_2,
       'User 3': user_3,
       'User 4': user_4}

# Use the dictionary to create a Pandas DataFrame
book_ratings = pd.DataFrame(dat)
print(book_ratings)

# If you created the dictionary correctly you should have a Pandas DataFrame
# that has column labels: 'Author', 'Book Title', 'User 1', 'User 2', 'User 3',
# 'User 4' and row indices 0 through 4.

# Now replace all the NaN values in your DataFrame with the average rating in
# each column. Replace the NaN values in place. HINT: you can use the fillna()
# function with the keyword inplace = True, to do this. Write your code below:

book_ratings.fillna(book_ratings.mean(), inplace=True)
print(book_ratings)
