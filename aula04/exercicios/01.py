import pandas as p
import matplotlib.pyplot as mpl

notas = [7, 8, 6, 9, 7, 5, 8, 7, 10, 6, 8, 9, 7, 5, 6, 8, 7, 9, 8, 10]

serie = p.Series(notas)
frequencia = serie.value_counts().sort_index()
frequencia_relativa = frequencia / len(notas)
frequencia_acumulada = frequencia.cumsum()

freq = ({
    'Frequencia Absoluta': frequencia,
    'Frequencia Relativa': frequencia_relativa,
    'Frequencia Acumulada': frequencia_acumulada
})

df = p.DataFrame(freq)

# mpl.bar(df['Frequencia Absoluta'], df['Frequencia Relativa'])
# mpl.xlabel('Frequencia Absoluta')
# mpl.ylabel('Frequencia Relativa')

frequencia.plot(kind='pie', autopct='%1.1f%%')

mpl.show()

