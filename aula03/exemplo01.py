import pandas as p

df = p.read_csv("clientes_ficticios_10000.csv")

# print(df.shape)
# print(df.head(4))

# print(amostra)
# print(amostra.shape)

# amostra = df.sample(n = 10, random_state = 15)
nAmostra = 1500
amostra = df.sample(n = nAmostra)
media_pop = df['idade'].mean()
media_amt = amostra['idade'].mean()

print(f"Média de idade da população: {media_pop:.2f}")
print(f"Média de idade da amostra: {media_amt:.2f}")

print(f"Erro amostral: {(media_pop - media_amt):.2f}")
