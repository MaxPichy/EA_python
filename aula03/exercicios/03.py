import pandas as p 

df = p.read_csv('clientes_ficticios_10000.csv')
base = df.sample(100, random_state = 7)
amostra10 = df.sample(10)
amostra30 = df.sample(30)

# print(amostra10[['nome', 'idade', 'valor_total_compras']])

media_pop = df['valor_total_compras'].mean()
media_amt10 = amostra10['valor_total_compras'].mean()
media_amt30 = amostra30['valor_total_compras'].mean()
desvio_amt10 = media_pop - media_amt10
desvio_amt30 = media_pop - media_amt30

print(f"Média popular de compra: {media_pop:.2f}")
print(f"Amostra (10): {amostra10[['nome', 'idade', 'valor_total_compras']]}")
print(f"Amostra (30): {amostra30[['nome', 'idade', 'valor_total_compras']]}")
print(f"Média amostra (10): {media_amt10:.2f}")
print(f"Média amostra (30): {media_amt30:.2f}")
print(f"Desvio padrão da amostra (10): {desvio_amt10:.2f}")
print(f"Desvio padrão da amostra (30): {desvio_amt30:.2f}")