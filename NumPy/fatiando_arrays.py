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

# IMPORTANTE: o fatiamento apenas cria uma view do array e não outra variável com o array fatiado
# para isso, deve-se usar a função copy()

# exemplo
mostra(X)
Z = X[:3, 2:]
mostra(Z)
Z[2, 2] = 155
mostra(Z)
mostra(X)

ZZ = np.copy(X[:3, 2:])
mostra(ZZ)
ZZ[2, 2] = 256
mostra(ZZ)
mostra(X)

# voltando o valor inicial em X
X[2, 4] = 15
mostra(X)

#outras funções
# diagonal

F = np.diag(X)
mostra(F)

T = np.diag(X, k=1)
mostra(T)

U = np.diag(X, k=-1)
mostra(U)

# função unique

P = np.array([[1, 3], [3, 2], [3, 4]])
mostra(P)

mostra(np.unique(P))

