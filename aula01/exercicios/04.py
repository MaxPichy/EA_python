import pandas as p
import matplotlib.pyplot as mpl

produtos = {
    'Produto': ['Arroz', 'Feijão', 'Café', 'Açúcar', 'Leite', 'Óleo', 'Macarrão'],
    'Preço': [32, 11, 24, 6, 8, 9, 7]
}

df = p.DataFrame(produtos)
mpl.bar(df['Produto'], df['Preço'], color='#55aa99')
mpl.title('Produtos')
mpl.xlabel('Produto')
mpl.ylabel('Preço')

mpl.show()
