import pandas as p
import matplotlib.pyplot as mpl

filmes = {
    'Filme': ['Avatar', 'Matrix', 'Interestelar', 'Vingadores', 'Barbie'],
    'Nota': [9.2, 9.5, 9.8, 8.9, 7.5]
}

df = p.DataFrame(filmes)
mpl.bar(df['Filme'], df['Nota'], color='#880033')

print(df)
print(df.head)
print(df.describe)
mpl.show()