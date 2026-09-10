import pandas as p

cpu = [45, 48, 46, 47, 49, 50, 46, 47, 48, 95]
# cpu = [45, 48, 46, 47, 49, 50, 46, 47, 48]
serie = p.Series(cpu)

ma = serie.sum() / len(cpu)
me = serie.median()
a = serie.max() - serie.min()
vp = serie.var(ddof=0)
dp = serie.std(ddof=0)

print(f'Média Aritmética: {ma:.2f}')
print(f'Mediana: {me:.2f}')
print(f'Amplitude: {a:.2f}')
print(f'Desvio Padrão Populacional: {dp:.2f}')
print("Estatísticamente, de acordo com os outros valores do conjunto, podemos perceber que o valor '95' é um outlier; sua presença impacta em 5 pontos na Média Aritmetica, 45 pontos na Amplitude e reduz 99% do Desvio Padrão.")