import pandas as pd

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


