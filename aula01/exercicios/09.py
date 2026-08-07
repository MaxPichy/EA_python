import pandas as p
import matplotlib.pyplot as mpl

pessoas = {
    'Nome': ['Anya', 'Joane', 'Dominic', 'Suzane', 'Yoshiki'],
    'Idade': [19, 24, 23, 32, 17]
}

df = p.DataFrame(pessoas)
mpl.bar(df['Nome'], df['Idade'], color='#0022ff')

mediaIdade = sum(pessoas['Idade']) / len(pessoas['Nome'])

print(len(pessoas['Nome']))
print(mediaIdade)
print(max(pessoas['Idade']))
print(min(pessoas['Idade']))
print(df.head)
print(df.info)
print(df.describe)
mpl.show()