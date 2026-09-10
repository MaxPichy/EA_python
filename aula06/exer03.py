import pandas as p

serverA = [100, 102, 98, 101, 99]
serverB = [70, 130, 90, 110, 100]

serieA = p.Series(serverA)
serieB = p.Series(serverB)

maA = serieA.sum() / len(serverA)
maB = serieB.sum() / len(serverB)
aA = serieA.max() - serieA.min()
aB = serieB.max() - serieB.min()
vpA = serieA.var(ddof=0)
vaA = serieA.var(ddof=1)
vpB = serieB.var(ddof=0)
vaB = serieB.var(ddof=1)
dpA = serieA.std(ddof=0)
dpB = serieB.std(ddof=0)

print(f'As Médias Aritméticas: \nServer A: {maA:.2f} \nServer B: {maB:.2f}')
print(f'As Amplitudes: \nServer A: {aA:.2f} \nServer B: {aB:.2f}')
print(f'Os Desvios Padrões: \nServer A: {dpA:.2f} \nServer B: {dpB:.2f}')
print('O Server A é mais estável, os números revelam que ele possui uma menor dispersão dos valores e mais previsibilidade de comportamento.')
