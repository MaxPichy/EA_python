import pandas as p
import matplotlib.pyplot as mpl

pessoas = {
    'Nome': ['João', 'Maria', 'Pedro', 'Ana', 'Lucas', 'Júlia', 'Carlos', 'Fernanda'],
    'Idade': [18, 20, 19, 22, 21, 18, 23, 20]
}

df = p.DataFrame(pessoas)
mpl.bar(df['Nome'], df['Idade'], color='#8800aa')
mpl.title('Pessoas')
mpl.xlabel('Nome')
mpl.ylabel('Idade')

print(df)
print(df.head(5))
df.info()
mpl.show()