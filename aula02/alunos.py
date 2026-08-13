import pandas as p

dados = {
    'Nome': ['Ana', 'Carlos', 'João', 'Felipe', 'Marcos', 'José'],
    'Idade': [20, 25, 63, 10, 58, 25],
    'Nota': [10, 5, 9, 8, 7, 3]
}

df = p.DataFrame(dados)

print(df[['Nome', 'Idade', 'Nota']])
print(df.iloc[0])
print(df.iloc[2:6])
print(df.iloc[4, 1])

# df['Nota_Final'] = 10
# df['Nota_Final'] = df['Nota'] + 0.8
# print(df['Nota_Final'])