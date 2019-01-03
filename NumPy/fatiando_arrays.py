import numpy as np


def pula_linha():
    print('\n')


def mostra(parametro):
    pula_linha()
    print(parametro)


# 1. ndarry[start:end]
# 2. ndarry[start:]
# 3. ndarry[:end]

X = np.arange(1, 21).reshape(4, 5)
mostra(X)

# linhas: [1, 2, 3], colunas [2, 3, 4]
Z = X[1:4, 2:5]
mostra(Z)

# outra maneira:
W = X[1:, 2:]
mostra(W)

# outra seleção:
J = X[:3, 2:]
mostra(J)


