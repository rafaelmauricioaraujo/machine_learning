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

# size retorna o tamanho do array
tamanho_array_2d = array_2d.shape
print('O tamanho do array é: {}'.format(tamanho_array_2d))
print('o tipo do da variável é: {}'.format(type(tamanho_array_2d)))

# a dimensão do array é referenciado pelo rank
# exemplo: um array de rank = 1:
strings = np.array(['Hello', 'World'])

# imprimindo o array
print('array de strings: ')
print(strings)

# imprimindos suas características

print(type(strings))
print(strings.shape)
print(strings.dtype)
print("este formato: '{}' é Unicode com 5 caracteres".format(strings.dtype))

# O arrays do NumPy sempre são do mesmo tipo, até quando é criado array com tipos variádos, o NumPy os converte

print('array de tipos variados')

tipos_variados = np.array(['Rafael', 1, 2.3, 'Teti'])
print(tipos_variados)

print('Suas caracteristicas: ')
print(type(tipos_variados))
print(tipos_variados.shape)
print(tipos_variados.dtype)

# é possível espeficicar o tipo de dado a ser preenchido no array, usado por questões de segurança ou performace

print('array espeficicando o tipo')

array_float = np.array([1.0, 2.2, 3.8], dtype=int)
print(array_float)

print('Salvando e abrindo arrays:')

outro_array = np.array([2, 4, 6, 8, 10])
np.save('array_teste', outro_array)

# abrindo o array salvo
array_carregado = np.load('array_teste.npy')

print('array_carregado = ', array_carregado)




