import numpy as np

resultados = np.random.randint(1, 7, size=10000)
quantidade_seis = np.sum(resultados == 6)

prob_experimental = (quantidade_seis / len(resultados))* 100
print(f"Frequência de 6s obtida: {quantidade_seis}")
print(f"Probabilidade Experimental: {prob_experimental:.2f}%")
print(f"Probabilidade Teórica (1/6): {(1/6)*100:.2f}%")