# importando o pandas
import pandas as pd

# Criando o dicionário de séries

itens = {'Bob': pd.Series(data=[245, 25, 55], index=['bike', 'roupas', 'relogio']),
         'Alice': pd.Series(data=[40, 110, 500, 45], index=['livro', 'oculos', 'bike', 'roupas'])}

# Exibindo o tipo para confirmar que é um dicionário
print(type(itens))

# Criando um DataFrame do Pandas, passando como parâmetro o dicionário de séries
carrinho_de_compras = pd.DataFrame(itens)
print(carrinho_de_compras)

# Criando um dicionário de Séries do Pandas sem índices
data = {'Bob': pd.Series([245, 25, 55]),
        'Alice': pd.Series([40, 110, 500, 45])}

# Criando um DataFrame
df = pd.DataFrame(data)

# Exibindo  o DataFrame
print(df)

# Também é possível obter algumas informações sobre o carrinho de compras
print('carrinho de compras.shape: ', carrinho_de_compras.shape)
print('carrinho de compras.ndim: ', carrinho_de_compras.ndim)
print('carrinho de compras tem um total de: ', carrinho_de_compras.size, 'elementos')
print()
print('os dados no carrinho de compras são: ', carrinho_de_compras.values)
print()
print('os indices das linhas no carrinho de compras são: ', carrinho_de_compras.index)
print()
print('os indices das colunas no carrinho de comrpas sao: ', carrinho_de_compras.columns)
