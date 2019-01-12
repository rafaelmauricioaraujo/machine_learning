# Pandas se trata de um pacote de manipulação de dados e análise em Python. O nome Pandas é derivado
# do termo econométrico painel de dados. O pandas incorpora duas estruturas de dados adicionais ao Python,
# ou seja, Séries Pandas e DataFrame pandas.

# importando pandas
import pandas as pd

# Criando uma série do Pandas que armazena uma lista de compras
lista_compras = pd.Series(data=[30, 6, 'Yes', 'No'], index=['Ovos', 'Maças', 'Leite', 'Pão'])

# Exibindo lista
print(lista_compras)
