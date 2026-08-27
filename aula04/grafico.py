import pandas as p
import matplotlib.pyplot as mpl

notas = [5, 6, 7, 8, 9, 10, 5, 6, 7, 8, 7, 8, 9, 10, 8, 7, 6, 8, 9, 8] 
serie = p.Series(notas) 
frequencia = serie.value_counts().sort_index()
frequencia.plot(kind='pie', autopct='%1.1f%%', color='#009999')
# mpl.xlabel('Notas')
# mpl.ylabel('Frequência')
mpl.title('Distribuição das Notas')

mpl.show()