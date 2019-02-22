import numpy as np

print('Alterando o rank de um array com a buil-in reshape')
array_1d = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19])
print(array_1d)
array_2d = np.reshape(array_1d, (4, 5))
print(array_2d)
print(array_2d.shape)
print("imprimindo [0,1]", array_2d[0, 1])


for i in range(array_2d.shape[1]):
    print(array_2d[0, i])


for i in range(array_2d.shape[1]):
    if array_2d[0, i] <= 2:
        print("menor que dois")
    elif array_2d[0, i] > 2:
        print("maior que dois")

for i in range(array_2d.shape[1]):
    if array_2d[0, i] <= 2:
        array_2d[0, i] = 0
    else:
        array_2d[0, i] = 1

for i in range(array_2d.shape[1]):
    print(array_2d[0, i])

