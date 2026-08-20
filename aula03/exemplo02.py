import numpy as np
import pandas as p

np.random.seed(15)
# Gera 10000 registros em torno de 70 com desvio padrão de 10:
dados = {'Notas': np.random.normal(70, 10, 10000)}
df = p.DataFrame(dados)

amostra = df.sample(n = 100, random_state = 42)

media_pop = df['Notas'].mean()
media_amt = amostra['Notas'].mean()
erro_amostral = media_pop - media_amt

print(f"Média da população: {media_pop:.2f}")
print(f"Média da amostra: {media_amt:.2f}")
print(f"Erro amostral: {erro_amostral:.2f}")

for tamanho in [10, 50, 100, 500, 1000]:
    amostra = df.sample(n = tamanho)
    media = amostra['Notas'].mean()

    print(tamanho, media)