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





