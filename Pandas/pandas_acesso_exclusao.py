# importando pandas
import pandas as pd

# Criando uma série do Pandas que armazena uma lista de compras
lista_compras = pd.Series(data=[30, 6, 'Yes', 'No'], index=['Ovos', 'Maças', 'Leite', 'Pão'])

# Exibindo lista
print(lista_compras)

# Podemos acessar a lista de compras usando rótulos de índices

# Utilizando um único rótulo de índices
print('Quantos ovos é preciso comprar: ', lista_compras['Ovos'])
print()

# Utilizando vários rótulos de índices
print('É preciso comprar pães e leite:\n', lista_compras[['Leite', 'Pão']])
print()

# É possível utilizar o 'loc' para acessar vários rótulos
print('Quantos ovos e maças comprar:\n', lista_compras.loc[['Ovos', 'Maças']])

# Acessando utilizando índices numéricos
print('Quantos ovos e maçãs compras: \n', lista_compras.iloc[[0, 1]])

# Utilizando um índice numérico negativo
print('É preciso comprar pães: \n', lista_compras[[-1]])

# Utilizando um índice numérico
print('Quantos ovos comprar: \n', lista_compras[0])

# Utilizando o 'iloc' parar acessar vários índices
print('é preciso comprar paes e leite: \n', lista_compras.iloc[[2, 3]])

# Alterando valores das listas

# imprimindo a lista original
print('Lista de compras: \n', lista_compras)

# alterando valores
lista_compras['Ovos'] = 2

# imprimindo nova lista
print('Lista de compras: \n', lista_compras)

# Removendo valores com o Series.drop e o Series.drop, inplace=True
# Exibindo a lista original
print('Lista de compras: \n', lista_compras)

# removendo um item utilizando o drop
print()
print('Lista de compras: \n', lista_compras.drop('Maças'))

# Removendo apenas na apresentação e não na lista original, esta maneira é chamada de out-of-place
# imprimindo a lista original
print('Lista de compras: \n', lista_compras)

# Para remover na original é preciso configurar o parâmetro inplace=True
# imprimindo a lista original
print()
print('Lista de compras: \n', lista_compras)

# Removendo na lista original
print()
print('lista de compras: \n', lista_compras.drop('Maças', inplace=True))

# Imprimindo a lista original
print('Lista de compras: \n', lista_compras)