import pandas as pd
import numpy as np

fruits = pd.Series([10, 6, 3], ['maças', 'laranjas', 'bananas'])

# Exibindo a lista para referência
print(fruits)

# É possível executar operações básicas, elemento a elemento usando simbolos aritméticos
print()
print('frutas + 2 \n', fruits + 2)
print()
print('frutas - 2 \n', fruits - 2)
print()
print('frutas * 2 \n', fruits * 2)
print()
print('frutas / 2 \n', fruits / 2)

# Também é possível aplicar funções matemáticas do NumPy, tais como 'sqrt(x)' a todos os elementos

# Exibindo a lista para referência
print(fruits)

# Aplicando diferentes funções matemáticas a todos os elementos
print()
print('EXP(X) = \n', np.exp(fruits))
print()
print('SQTR(X) = \n', np.sqrt(fruits))
print()
print('POW(X) = \n', np.power(fruits, 2))

# Também é possível aplicar operações matemáticas apenas a itens selecionados em uma lista

# Exibindo a lista para referência
print(fruits)

# Adicionando 2 apenas a banana
print('Qtde de bananas + 2', fruits['bananas'] + 2)
print()

# Subtraíndo 2 maças
print('Qtde de maças - 2', fruits['maças'] - 2)
print()

# Multiplicando maças e laranjas por 2
print('Dobrando a qtde de maças e laranjas: \n', fruits[['maças', 'laranjas']] * 2)
print()

# Dividindo maças e laranjas por 2
print('Dividinso o número de laranjas: \n', fruits[['maças', 'laranjas']] / 2)
print()

# Também é possível aplicar operações sobre a série do Pandas com dados de tipos variados, desde
# a operação seja definida para todos os tipos de dados, caso contrário lançará um erro

# lista de compras
lista_compras = pd.Series(data=[30, 6, 'Yes', 'No'], index=['Ovos', 'Maças', 'Leite', 'Pão'])

# multiplicando a lista por 2
print('Duplicando a lista de compras: \n', lista_compras * 2)

# Outro exemplo:

# Create a Pandas Series that contains the distance of some planets from the Sun.
# Use the name of the planets as the index to your Pandas Series, and the distance
# from the Sun as your data. The distance from the Sun is in units of 10^6 km

distance_from_sun = [149.6, 1433.5, 227.9, 108.2, 778.6]

planets = ['Earth', 'Saturn', 'Mars', 'Venus', 'Jupiter']

# Create a Pandas Series using the above data, with the name of the planets as
# the index and the distance from the Sun as your data.
dist_planets = pd.Series([149.6, 1433.5, 227.9, 108.2, 778.6], ['Earth', 'Saturn', 'Mars', 'Venus', 'Jupiter'])
print(dist_planets)

# Calculate the number of minutes it takes sunlight to reach each planet. You can
# do this by dividing the distance from the Sun for each planet by the speed of light.
# Since in the data above the distance from the Sun is in units of 10^6 km, you can
# use a value for the speed of light of c = 18, since light travels 18 x 10^6 km/minute.
time_light = dist_planets / 18
print(time_light)

# Use Boolean indexing to select only those planets for which sunlight takes less
# than 40 minutes to reach them.
close_planets = time_light[time_light < 40]
print(close_planets)






