import pandas as p

alunos = p.DataFrame({
 "Nome": ["Ana", "Bruno", "Carlos", "Daniela", "Eduardo", "Fernanda", "Gabriel", "Helena", "Igor", "Julia", "Lucas", "Marina"],
 "Nota": [8, 7, 9, 6, 10, 8, 7, 9, 5, 8, 6, 10]
})

df = p.DataFrame(alunos)
amostra5 = df.sample(5)
amostra8 = df.sample(8)

media_pop = df['Nota'].mean()
media_amt5 = amostra5['Nota'].mean()
media_amt8 = amostra8['Nota'].mean()
desvio_amt5 = media_pop - media_amt5
desvio_amt8 = media_pop - media_amt8

print(f"Tamanho: {df.shape}")
print(f"Média popular: {media_pop:.2f}")
print(f"Média amostra (5): {media_amt5:.2f}")
print(f"Média amostra (8): {media_amt8:.2f}")
print(f"Desvio padrão da amostra (5): {desvio_amt5:.2f}")
print(f"Desvio padrão da amostra (8): {desvio_amt8:.2f}")