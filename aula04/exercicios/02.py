import pandas as p
import matplotlib.pyplot as mpl

lan = ['Java', 'Python', 'JavaScript', 'C', 'C++', 'PHP', 'Assembly', 'Java', 'Python', 'JavaScript', 'C', 'Java', 'PHP', 'Python', 'Python', 'Python', 'C', 'C', 'C++', 'Javascript']

serie = p.Series(lan)

frequencia = serie.value_counts().sort_index()
frequencia_relativa = frequencia / int(len(lan))
frequencia_acumulada = frequencia.cumsum()

mpl.bar(serie.iloc[0:29].unique(), frequencia_relativa * 100, color='#449933')

print(frequencia)
print(frequencia_relativa)
print(frequencia_relativa.idxmax())
mpl.show()
