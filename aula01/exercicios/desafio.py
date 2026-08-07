import pandas as p

produtos = {
    'Produto': ['Arroz', 'Feijão', 'Café', 'Açúcar', 'Leite', 'Óleo', 'Macarrão'],
    'Preço': [25.99, 11.25, 24.49, 3.99, 5.49, 9.80, 4.25],
    'Estoque': [4, 7, 9, 12, 23, 3, 13]
}

df = p.DataFrame(produtos)
df.insert(loc=3, column='Valor_Estoque', value= df['Preço'] * df['Estoque'])

print(df)