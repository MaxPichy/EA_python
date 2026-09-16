import numpy as n
import pandas as p

reqs = n.random.choice(['Sucesso', 'Erro'], size=10000, p=[0.95, 0.05])
serie = p.Series(reqs)

erros = (serie == 'Erro').sum()
p_erros = erros / 100

print(f'Requisições: 10.000')
print(f'Erros: {erros}')
print(f'% Erros: {p_erros:.2f}%')