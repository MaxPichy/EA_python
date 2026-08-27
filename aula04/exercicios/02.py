import pandas as p
import matplotlib.pyplot as mpl

lan = ['Java'] * 2 + ['Python'] * 8 + ['JavaScript'] * 9 + ['C'] * 4 + ['C++'] * 2 + ['PHP'] * 3 + ['Assembly'] * 2

serie = p.Series(lan)

frequencia = serie.value_counts()
frequencia_relativa = frequencia / len(lan)
frequencia_acumulada = serie.cumsum()

freq = ({
    'Frequencia': frequencia,
    'Frequencia Relativa': frequencia_relativa,
    'Frequencia Acumulada': frequencia_acumulada
})

df = p.DataFrame(freq)
