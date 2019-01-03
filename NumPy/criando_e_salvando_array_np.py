import numpy as np

array = np.array([1, 2, 3, 4, 5])

# imprimindo o array

print(array)

# imprimindo o tipo do array
print(type(array))

# dtype imprime como os elementos do array estão alocados na memória
print(array.dtype)

# shape retorna o número de dimensões do array em uma tupla
# no caso, o array tem apenas uma dimensao contendo cinco elementos
print(array.shape)

# array bidimensional
array_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9, ], [10, 11, 12]])

# imprimindo o array bidimensional
print(array_2d)

# usando o comando shape para ver as dimensões do array
print(array_2d.shape)

