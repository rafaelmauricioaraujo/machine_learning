import numpy as np


def pula_linha():
    print('')


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
# linhas: [1 até o final], colunas [2 até o final]
W = X[1:, 2:]
mostra(W)

# outra seleção:
# linhas: [inicio até o a segunda], colunas [2 até o final]
J = X[:3, 2:]
mostra(J)

# linhas: [todas], colunas [terceira]
R = X[:, 2]
mostra(R)

# agora o mesmo mas em uma coluna
H = X[:, 2:3]
mostra(H)




