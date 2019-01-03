import numpy as np

X = np.arange(25).reshape(5, 5)
print(X)

print(X[X > 10])

print(X[X <= 7])

print(X[(X < 10) & (X >= 7)])

(X[(X < 5) & (X >= 0)]) = 1
print(X)


