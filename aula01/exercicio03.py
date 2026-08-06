import pandas as p
import matplotlib.pyplot as mplib

washitong = {
    'Produto': ['Folks of Air', 'Hunger Games', 'Harry Potter', 'Demian', 'Red Queen', 'Brás Cubas', 'Odisseia'],
    'Preço': [99.99, 65.99, 124.99, 28.50, 238.99, 33.49, 42.89],
    'Quantidade': [3, 5, 9, 15, 4, 22, 6]
}

df = p.DataFrame(washitong)

# mplib.bar(df['Produto'], df['Preço'],
#           width = 0.5,
#           color='#660099'
# )

# mplib.plot(df['Produto'], df['Preço'],
#          color='#660099')

mplib.bar(df['Produto'], df['Quantidade'],
          width = 0.5,
          color='#660099'
)


mplib.title('Wa Shi Tong - Preços')
mplib.xlabel('Produto')
# mplib.ylabel('Preço')
mplib.ylabel('Quantidade')

print(df)
mplib.show()
