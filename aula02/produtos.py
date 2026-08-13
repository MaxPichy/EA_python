import pandas as p

dados = {
    'Produto': ['Mouse', 'Teclado', 'Monitor', 'Gabinete'],
    'Preço': [80, 50, 800, 250],
    'Quantidade': [10, 50, 15, 25]
}

df = p.DataFrame(dados)

df['Valor_Estoque'] = df['Preço'] * df['Quantidade']

print(df)
print(df.sort_values('Valor_Estoque', ascending = False))
print(df['Quantidade'] < 20)
print(df[(df['Quantidade'] < 20) & (df['Preço'] < 300)])