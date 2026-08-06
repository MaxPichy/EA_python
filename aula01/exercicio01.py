import pandas as p

dados = {
    'Nome': ['João', 'Maria', 'Pedro', 'Ana'],
    'Idade': [18, 20, 19, 22]
}

df = p.DataFrame(dados)

# Exibir o DataFrame
print(df)

# Contar os registros do DataFrame
print(len(df)) # Forma 1
print(df.shape) # Forma 2

# Vizualizar as informações do DataFrame
df.info()