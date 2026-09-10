import pandas as p

dados =  [110, 115, 120, 112, 118, 121, 117, 113, 119, 300]
# dados =  [110, 115, 120, 112, 118, 121, 117, 113, 119]
serie = p.Series(dados)

ma = serie.sum() / len(dados)
me = serie.median()
a = serie.max() - serie.min()
vp = serie.var(ddof=0)
dp = serie.std(ddof=0)

print(f'Média Aritmética X Mediana: {ma:.2f} X {me:.2f}')
print(f'Amplitude: {a:.2f}')
print(f'Variância Populacional: {vp:.2f}')
print(f'Desvio Padrão Populacional: {dp:.2f}')
print("Estatísticamente, de acordo com os outros valores do conjunto, podemos perceber que o valor '300' é um outlier; sua presença impacta em 179 pontos na Amplitude, mais de 3000 pontos na Variância Populacional e 51 pontos no Desvio Padrão.")