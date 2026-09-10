import pandas as p

computadorA = [4.0, 4.1, 4.0, 4.2, 4.1]
computadorB = [2.0, 5.0, 3.0, 6.0, 4.0]

serieA = p.Series(computadorA)
serieB = p.Series(computadorB)

maA = serieA.sum() / len(computadorA)
maB = serieB.sum() / len(computadorB)
aA = serieA.max() - serieA.min()
aB = serieB.max() - serieB.min()
vpA = serieA.var(ddof=0)
vaA = serieA.var(ddof=1)
vpB = serieB.var(ddof=0)
vaB = serieB.var(ddof=1)
dpA = serieA.std(ddof=0)
dpB = serieB.std(ddof=0)

print(f'As Médias Aritméticas: \nComputador A: {maA:.2f} \nComputador B: {maB:.2f}')
print(f'Os Desvios Padrões: \nComputador A: {dpA:.2f} \nComputador B: {dpB:.2f}')
print('De acordo com a Média e Desvio Padrão apresentados, o Computador A é mais estável; ele apresenta um Desvio Padrão menor.')
print('Um consumo mais variado de memória RAM pode indicar várias coisas, na verdade. Entre elas abertura de arquivos executáveis ou não ou até mesmo algum tipo de malware operando.')