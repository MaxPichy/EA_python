import pandas as p

produtos = {
    'Produto': ['Mouse', 'Teclado', 'Monitor', 'Webcam', 'Headset'],
    'Categoria': ['Periférico', 'Periférico', 'Vídeo', 'Vídeo', 'Áudio'],
    'Preço': [80, 120, 900, 250, 300],
    'Quantidade': [10, 8, 4, 6, 5]
}

df = p.DataFrame(produtos)

df['Valor_Estoque'] = df['Preço'] * df['Quantidade']

print(df.iloc())