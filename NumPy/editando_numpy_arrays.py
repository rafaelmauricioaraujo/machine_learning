import numpy as np

array = np.array([1, 2, 3, 4, 5])
print(array)

print('Acessando elementos pelos índices')

print('array[0]: ', array[0])
print('array[1]: ', array[1])
print('array[4]: ', array[4])

print('Também é possível espeficifar índices negativos para acessar a partir do final')

print('array[-5]: ', array[-5])
print('array[-4]: ', array[-4])
print('array[-1]: ', array[-1])

print('Alterando valor de um elemento')
print('array[3] = 20')
array[3] = 20
print(array)

print('Também é possível acessar e alterar valores de um array bidimensional')

matriz = np.arange(1, 10).reshape((3, 3))
print(matriz)
print('elemento na posicao (0, 0)', matriz[0, 0])
print('elemento na posicao (1, 2)', matriz[1, 2])
print('elemento na posicao (2, 2)', matriz[2, 2])

print('Alterando valores na matriz')
matriz[0, 0] = 20
print(matriz)

X = np.arange(1, 10).reshape(3, 3)
print(X)
# axis = 0: selecionar da linha enquanto axis = 1: selecionar da coluna
Y = np.delete(X, 2, axis=1)
print('\n', Y)
Z = np.delete(Y, 0, axis=0)
print('\n', Z)

print('Adicionando elementos com a função append')

elementos = np.array([1, 2, 3])
print(elementos)
elementos = np.append(elementos, [4])
print(elementos)
elementos = np.append(elementos, [5, 6, 7])
print(elementos)

print('Adicionando em matrizes')

M = np.arange(11, 20).reshape(3, 3)
print(M)
V = np.append(M, [[14], [17], [20]], axis=1)
print(V)

print('Usando a função insert')
vetor = np.array([1, 2, 3, 4, 5, 6])
print(vetor)
vetor = np.insert(vetor, 2, [3, 4])
print(vetor)

print('Agora em uma matriz')
outra_matriz = np.array([[1, 2], [5, 6]])
print(outra_matriz)
outra_matriz = np.insert(outra_matriz, 1, [3, 4], axis=0)
print(outra_matriz)
outra_matriz = np.insert(outra_matriz, 2, [3, 5, 7], axis=1)
print(outra_matriz)

print('Utilizando a função vstack para empilhar arrays')
# Criamos uma ndarray de ordem 1
x = np.array([1, 2])

# Criamos uma ndarray de ordem 2
Y = np.array([[3, 4], [5, 6]])

# Vamos exibir o x
print()
print('x = ', x)

# Vamos exibir o Y
print()
print('Y = \n', Y)

# Empilhamos x sobre Y
z = np.vstack((x, Y))

# Empilhamos x à direita de Y. Precisamos remodelar x para poder empilhá-lo à direita de Y.
w = np.hstack((Y, x.reshape(2, 1)))

# Vamos exibir o v
print()
print('z = \n', z)

# Vamos exibir o w
print()
print('w = \n', w)
