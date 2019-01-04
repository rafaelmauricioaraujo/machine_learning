# import NumPy into Python
import numpy as np
from sklearn.metrics import r2_score


# Create a 1000 x 20 ndarray with random integers in the half-open interval [0, 5001).
X = np.random.randint(0, 5001, (1000, 20))

# print the shape of X
print(X.shape)

# Average of the values in each column of X
ave_cols = X.mean(axis=0)

# Standard Deviation of the values in each column of X
std_cols = X.std(axis=0)

# Print the shape of ave_cols
print(ave_cols.shape)

# Print the shape of std_cols
print(std_cols.shape)

# Mean normalize X
X_norm = (X - ave_cols)/std_cols

# Print the average of all the values of X_norm
print(X_norm.mean())

# Print the average of the minimum value in each column of X_norm
print(X_norm.min())

# Print the average of the maximum value in each column of X_norm
print(X_norm.max())

# We create a random permutation of integers 0 to 4
print(np.random.permutation(5))

print('A partir daqui são testes para resolução do row_indices')
primeiro = np.random.permutation(9).reshape(3, 3)
print(primeiro)
print(primeiro.dtype)
print(primeiro.shape[0])

# Create a rank 1 ndarray that contains a random permutation of the row indices of `X_norm`
row_indices = np.arange(np.random.permutation(primeiro.shape[0]))
print('row_indices: ')
print(row_indices)
