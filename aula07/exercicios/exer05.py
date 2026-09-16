import numpy as n
import pandas as p

lancamentos = n.random.randint(1, 7, 10000)
serie = p.Series(lancamentos)

q_um = (serie == 1).sum()
q_dois = (serie == 2).sum()
q_tres = (serie == 3).sum()
q_quatro = (serie == 4).sum()
q_cinco = (serie == 5).sum()
q_seis = (serie == 6).sum()

print(f'freq_relativa:\n 1 {(q_um/10000)*100:.2f}\n 2 {(q_dois/10000)*100:.2f}\n 3 {(q_tres/10000)*100:.2f}\n 4 {(q_quatro/10000)*100:.2f}\n 5 {(q_cinco/10000)*100:.2f}\n 6 {(q_seis/10000)*100:.2f}')
print(f'freq_teorica: {(1/6)*100:.2f}')
