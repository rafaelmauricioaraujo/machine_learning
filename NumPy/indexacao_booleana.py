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

# Vamos criar uma ndarray desordenada de ordem 1
x = np.random.randint(1, 11, size=(10,))

# Vamos exibir o x
print()
print('Original x = ', x)

# Ordenamos x e exibimos a array ordenada após usar `sort` como uma função.
print()
print('Sorted x (out of place):', np.sort(x))

# Quando ordenamos fora do lugar, a array original permanece intacta. Para ver isso, podemos imprimir x novamente
print()
print('x after sorting:', x)

# Ordenamos x mas mantendo apenas elementos únicos
print()
print(np.sort(np.unique(x)))

# Vamos criar uma ndarray desordenada de ordem 1
x = np.random.randint(1, 11, size=(10,))

# Vamos exibir o x
print()
print('Original x = ', x)

# Ordenamos x e exibimos a array ordenada após usar `sort` como um método.
x.sort()

# Quando usamos o sort como método da instância de ndarray, a array original é alterada para uma array ordenada.
# Para ver isso, podemos imprimir x novamente
print()
print('x after sorting:', x)

# Vamos criar uma ndarray desordenada de ordem 2
X = np.random.randint(1, 11, size=(5, 5))

# Vamos exibir o X
print()
print('Original X = \n', X)
print()

# Ordenamos X por suas colunas e exibimos a array ordenada
print()
print('X with sorted columns :\n', np.sort(X, axis=0))

# Ordenamos X por suas linhas e exibimos a array ordenada
print()
print('X with sorted rows :\n', np.sort(X, axis=1))
