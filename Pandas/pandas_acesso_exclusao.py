# importando pandas
import pandas as pd

# Criando uma série do Pandas que armazena uma lista de compras
lista_compras = pd.Series(data=[30, 6, 'Yes', 'No'], index=['Ovos', 'Maças', 'Leite', 'Pão'])

# Exibindo lista
print(lista_compras)

# Podemos acessar a lista de compras usando rótulos de índices

# Utilizando um único rótulo de índices
print('Quando ovos é preciso comprar: ', lista_compras['Ovos'])


