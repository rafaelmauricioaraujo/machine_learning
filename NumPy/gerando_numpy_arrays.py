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
print('usando apenas um parametro: stop')

primeiro = np.arange(10)
print(primeiro)
print(primeiro.dtype)

print('usando dois parametros: start, stop')
segundo = np.arange(5, 11)
print(segundo)

print('Usando três parametros: start, stop, step')
terceiro = np.arange(1, 20, 3)
print(terceiro)

print('Utilizando a buil-in linespace a qual exige pelo menos dois parametros')
outro_array = np.linspace(0, 25, 10)
print(outro_array)
print('10 números de 0 a 25, igualmente espaçados')

print("Exlcuindo o último número")
mais_outro = np.linspace(0, 25, 10, endpoint=False)
print(mais_outro)
print(mais_outro.dtype)

print('Alterando o rank de um array com a buil-in reshape')
array_1d = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19])
print(array_1d)
array_2d = np.reshape(array_1d, (4, 5))
print(array_2d)
