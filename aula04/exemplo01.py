import pandas as p

tabela = p.read_csv('clientes_ficticios_10000.csv')
# print(tabela.head(10))

serie = tabela['estado']
frequencia = serie.value_counts()
frequencia_acumulada = frequencia.cumsum()

freq = p.DataFrame({
    'Frequência': frequencia,
    'Frequência Relativa': (frequencia / len(tabela)) * 100,
    'Frequência Acumulada': frequencia_acumulada
})

print(freq)


