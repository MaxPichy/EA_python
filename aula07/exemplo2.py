import numpy as np

resultado_unico = np.random.randint(1, 7)
print(f"Resultado do lançamento: {resultado_unico}")

lancamentos_1000 = np.random.randint(1, 7, size=1000)
print(f"Primeiros 10 lançamentos: {lancamentos_1000[:10]}")
print(f"Total de lançamentos realizados: {len(lancamentos_1000)}")