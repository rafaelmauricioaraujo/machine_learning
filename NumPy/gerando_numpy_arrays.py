import numpy as np

minha_lista = [1, 3, 5, 7, 9]
print(np.array(minha_lista))
print(np.array(minha_lista).dtype)

print('criando um array de zeros com função build-in numpy np.zeros')
zero_array = np.zeros((3, 4))
print(zero_array)
print(zero_array.dtype)

print('também é possível espeficicar o tipo dos elementos do array')
zero_array_int = np.zeros((3, 4), int)
print(zero_array_int)
print(zero_array_int.dtype)

print('Criando um array de uns com np.ones')
ones_array = np.ones((3, 4))
print(ones_array)
print(ones_array.dtype)

print('Criando um array de constantes através da build-in np.full')
fives_array = np.full((3, 4), 5)
print(fives_array)
print(fives_array.dtype)

print('Criando uma matriz indentidade através da build-in np.eyes')
matriz_identidade = np.eye(5)
print(matriz_identidade)

print('Criando uma matriz diagonal através da build-in np.diag')
matriz_diagonal = np.diag([2, 4, 8, 10])
print(matriz_diagonal)

print('Criando arrays com a build-in arange')
print('usando apenas um parametro')

primeiro = np.arange(10)
print(primeiro)
print(primeiro.dtype)
