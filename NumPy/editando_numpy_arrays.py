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
