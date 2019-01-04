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

print('Utilizando o métodos encadeados do NumPy')
Y = np.arange(20).reshape((10, 2))
print(Y)
print('Outro exemplo')
Z = np.linspace(0, 50, 10, endpoint=False).reshape(5, 2)
print(Z)

print('Criando arrays de números aleatórios')
print('usando a .random para criar floats aleatorios entre 0(inclusivo) e 1(exclusivo')

floats_aleatorios = np.random.random((3, 3))
print(floats_aleatorios)

print('Criando inteiros aleatórios dentro de um intervalo')
ints_aleatorios = np.random.randint(4, 15, (3, 2))
print(ints_aleatorios)

print('Criando a partir de distribuições estatísticas')
dist_normal = np.random.normal(0, 0.1, size=(1000, 1000))
print(dist_normal)
print('array bidimensional de 1000 linhas por 1000 colunas com média=0 e dp=0.1')

print('Caracteristicas: ')
print('média: ', dist_normal.mean())
print('desvio padrão: ', dist_normal.std())
print('máximo: ', dist_normal.max())
print('mínimo: ', dist_normal.min())
print('nº de positivos: ', (dist_normal > 0).sum())
print('nº de negativos: ', (dist_normal < 0).sum())


# testando
print('testando')
row_indices = np.array(np.random.permutation(dist_normal.shape))
print(row_indices)
