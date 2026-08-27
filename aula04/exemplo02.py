import pandas as p
import matplotlib.pyplot as mpl

tempos = [120, 130, 115, 140, 150, 180, 175, 190, 210, 220, 250, 280, 300, 320, 350]

mpl.hist(tempos, bins=5)
mpl.xlabel("Tempo de resposta (ms)")
mpl.ylabel("Frequência")
mpl.title("Tempo de Resposta do Sistema")
mpl.show()