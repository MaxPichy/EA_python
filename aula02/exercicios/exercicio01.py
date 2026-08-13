import pandas as p

produtos = {
    'Produto': ['Mouse', 'Teclado', 'Monitor', 'Webcam', 'Headset'],
    'Categoria': ['Periférico', 'Periférico', 'Vídeo', 'Vídeo', 'Áudio'],
    'Preço': [80, 120, 900, 250, 300],
    'Quantidade': [10, 8, 4, 6, 5]
}

df = p.DataFrame(produtos)

print(df)
print(df.shape)
df.info()
df.describe()
print(df[['Produto', 'Preço']])
print(df.iloc[0:2])
print(df.iloc[2])