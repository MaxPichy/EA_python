import pandas as p

produtos = {
    'Produto': ['Mouse', 'Teclado', 'Monitor', 'Webcam', 'Headset'],
    'Preço': [85, 150, 980, 220, 320],
    'Quantidade': [12, 8, 4, 10, 6]
}

df = p.DataFrame(produtos)

print(len(produtos['Produto']))
print(max(produtos['Preço']))
print(min(produtos['Preço']))
print(sum(produtos['Quantidade']))