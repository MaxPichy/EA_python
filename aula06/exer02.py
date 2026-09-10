import pandas as p

grupoA = [100, 100, 100, 100, 100]
grupoB = [80, 90, 100, 110, 120]

serieA = p.Series(grupoA)
serieB = p.Series(grupoB)

maA = serieA.sum() / len(grupoA)
maB = serieB.sum() / len(grupoB)
aA = serieA.max() - serieA.min()
aB = serieB.max() - serieB.min()
vpA = serieA.var(ddof=0)
vaA = serieA.var(ddof=1)
vpB = serieB.var(ddof=0)
vaB = serieB.var(ddof=1)
dpA = serieA.std(ddof=0)
dpB = serieB.std(ddof=0)

print(f'As Médias Aritméticas: \nGrupo A: {maA:.2f} \nGrupo B: {maB:.2f}')
print(f'As Amplitudes: \nGrupo A: {aA:.2f} \nGrupo B: {aB:.2f}')
print(f'As Variâncias Amostrais X Populacionais: \nGrupo A: {vaA:.2f} X {vpA:.2f} \nGrupo B: {vaB:.2f} X {vpB:.2f}')
print(f'Os Desvios Padrões: \nGrupo A: {dpA:.2f} \nGrupo B: {dpB:.2f}')
print('O Grupo B possui um valor de dispersão maior, por conta de uma maior diferença entre os valores presentes no conjunto.')
