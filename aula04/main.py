import pandas as p

notas = [7, 8, 6, 9, 7, 5, 8, 7, 10, 6, 8, 9, 7, 5, 6, 8, 7, 9, 8, 10]

serie = p.Series(notas)

frequencia = serie.value_counts().sort_index()
frequencia_acumulada = frequencia.cumsum()

# print(frequencia_acumulada)

tabela = p.DataFrame({
    'Frequência': frequencia,
    'Frequência Relativa': frequencia / len(serie),
    'Frequência Acumulada': frequencia_acumulada
})

print(tabela)