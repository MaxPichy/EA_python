import pandas as p

dados = [10, 12, 15, 18, 20]
serie = p.Series(dados)

ma = serie.sum() / len(dados)
a = serie.max() - serie.min()
vp = serie.var(ddof=0)
dp = serie.std(ddof=0)

print(f'Média Aritmética: {ma:.2f}')
print(f'Amplitude: {a:.2f}')
print(f'Variância Populacional: {vp:.2f}')
print(f'Desvio Padrão Populacional: {dp:.2f}')