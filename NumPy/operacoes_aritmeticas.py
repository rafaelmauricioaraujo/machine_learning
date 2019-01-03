import numpy as np


def pula_linha():
    print()


def mostra(p):
    pula_linha()
    print(p)


x = np.array([1, 2, 3, 4])
y = np.array([5.5, 6.5, 7.5, 8.5])

mostra('x: {}'.format(x))
mostra('y: {}'.format(y))

mostra('x + y : {}'.format(x + y))
mostra('np.add(x, y) : {}'.format(np.add(x, y)))

mostra('x - y : {}'.format(x - y))
mostra('np.subtract(x, y) : {}'.format(np.subtract(x, y)))

mostra('x * y : {}'.format(x * y))
mostra('np.multiply(x, y) : {}'.format(np.multiply(x, y)))

mostra('x / y : {}'.format(x / y))
mostra('np.divide(x, y) : {}'.format(np.divide(x, y)))

# arrays de duas dimensões

X = np.array([1, 2, 3, 4]).reshape(2, 2)
Y = np.array([5.5, 6.5, 7.5, 8.5]).reshape(2, 2)

print()
print('X = \n', X)

print()
print('Y = \n', Y)
print()

# Executamos operações básicas, elemento a elemento, usando símbolos aritméticos e funções
print('X + Y = \n', X + Y)
print()
print('add(X,Y) = \n', np.add(X, Y))
print()
print('X - Y = \n', X - Y)
print()
print('subtract(X,Y) = \n', np.subtract(X, Y))
print()
print('X * Y = \n', X * Y)
print()
print('multiply(X,Y) = \n', np.multiply(X, Y))
print()
print('X / Y = \n', X / Y)
print()
print('divide(X,Y) = \n', np.divide(X, Y))

# Criamos uma ndarray de ordem 1
x = np.array([1, 2, 3, 4])

# Vamos exibir o x
print()
print('x = ', x)

# Aplicamos diferentes funções matemáticas para todos os elementos de x
print()
print('EXP(x) =', np.exp(x))
print()
print('SQRT(x) =', np.sqrt(x))
print()
print('POW(x,2) =', np.power(x, 2)) # Elevamos todos os elementos para a potência de 2


# funções estatísticas
# Vamos criar uma ndarray de formato 2 x 2
X = np.array([[1,2], [3,4]])

# Vamos exibir o x
print()
print('X = \n', X)
print()

print('Average of all elements in X:', X.mean())
print('Average of all elements in the columns of X:', X.mean(axis=0))
print('Average of all elements in the rows of X:', X.mean(axis=1))
print()
print('Sum of all elements in X:', X.sum())
print('Sum of all elements in the columns of X:', X.sum(axis=0))
print('Sum of all elements in the rows of X:', X.sum(axis=1))
print()
print('Standard Deviation of all elements in X:', X.std())
print('Standard Deviation of all elements in the columns of X:', X.std(axis=0))
print('Standard Deviation of all elements in the rows of X:', X.std(axis=1))
print()
print('Median of all elements in X:', np.median(X))
print('Median of all elements in the columns of X:', np.median(X,axis=0))
print('Median of all elements in the rows of X:', np.median(X,axis=1))
print()
print('Maximum value of all elements in X:', X.max())
print('Maximum value of all elements in the columns of X:', X.max(axis=0))
print('Maximum value of all elements in the rows of X:', X.max(axis=1))
print()
print('Maximum value of all elements in X:', X.min())
print('Maximum value of all elements in the columns of X:', X.min(axis=0))
print('Maximum value of all elements in the rows of X:', X.min(axis=1))

# adicionando apenas um número a todos os elementos

# Vamos criar uma ndarray de formato 2 x 2
X = np.array([[1,2], [3,4]])

# Vamos exibir o x
print()
print('X = \n', X)
print()

print('3 * X = \n', 3 * X)
print()
print('3 + X = \n', 3 + X)
print()
print('X - 3 = \n', X - 3)
print()
print('X / 3 = \n', X / 3)

# broadcasting

# Criamos uma ndarray de ordem 1
x = np.array([1,2,3])

# Criamos uma ndarray 3x3
Y = np.array([[1,2,3],[4,5,6],[7,8,9]])

# Criamos uma ndarray 3x1
Z = np.array([1,2,3]).reshape(3,1)

# Vamos exibir o x
print()
print('x = ', x)
print()

# Vamos exibir o Y
print()
print('Y = \n', Y)
print()

# Vamos exibir o Z
print()
print('Z = \n', Z)
print()

print('x + Y = \n', x + Y)
print()
print('Z + Y = \n',Z + Y)




