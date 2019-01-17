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






