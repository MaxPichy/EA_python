import pandas as p
import matplotlib.pyplot as mpl

idades = [18, 19, 20, 21, 22, 25, 27, 30, 31, 35, 40, 50, 60, 61, 62, 63]
mpl.hist(idades, bins=5)
mpl.xlabel("Idade")
mpl.ylabel("Frequência")
mpl.title("Distribuição das Idades")

mpl.show()