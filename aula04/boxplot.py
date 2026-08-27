import pandas as p
import matplotlib.pyplot as mpl

tempos = [120, 130, 115, 140, 150, 180, 175, 190, 210, 220, 250, 280, 300, 320, 350]

mpl.boxplot(tempos)
mpl.ylabel("Tempo (ms)")
mpl.title("Distribuição do Tempo de Resposta")
mpl.show()