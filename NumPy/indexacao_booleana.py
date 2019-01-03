import numpy as np

X = np.arange(25).reshape(5, 5)
print(X)

print(X[X > 10])

print(X[X <= 7])

print(X[(X < 10) & (X >= 7)])

(X[(X < 5) & (X >= 0)]) = 1
print(X)

# funções de conjunto usando array

x = np.array([1, 2, 3, 4, 5])
y = np.array([6, 7, 2, 8, 4])

print(np.intersect1d(x, y))
print(np.setdiff1d(x, y))
print(np.union1d(x, y))


