import numpy as np

minha_lista = [1, 3, 5, 7, 9]
print(np.array(minha_lista))
print(np.array(minha_lista).dtype)

print('criando um array de zeros com função build-in numpy')
zero_array = np.zeros((3, 4))
print(zero_array)
print(zero_array.dtype)

print('também é possível espeficicar o tipo dos elementos do array')
zero_array_int = np.zeros((3, 4), int)
print(zero_array_int)
print(zero_array_int.dtype)
