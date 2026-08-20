import pandas as p 

alunos = p.DataFrame({
 "Nome": ["Ana", "Bruno", "Carlos", "Daniela", "Eduardo", "Fernanda", "Gabriel", "Helena", "Igor", "Julia", "Lucas", "Marina", "Lurdes", "Ivan", "Eva", "Ana", "Bruno", "Carlos", "Daniela", "Eduardo", "Fernanda", "Gabriel", "Helena", "Igor", "Julia", "Lucas", "Marina", "Lurdes", "Ivan", "Eva"],
 "Idade": [18, 19, 62, 40, 17, 19, 20, 23, 27, 53, 18, 19, 62, 40, 17, 19, 20, 23, 27, 53, 18, 19, 62, 40, 17, 19, 20, 23, 27, 53],
 "Nota": [8, 7, 9, 6, 10, 8, 7, 9, 5, 8, 6, 10, 4, 9, 6, 8, 7, 9, 6, 10, 8, 7, 9, 5, 8, 6, 10, 4, 9, 6]
})

df = p.DataFrame(alunos)
amostra5 = df.sample(5)
amostra10 = df.sample(10)

media_pop = df['Nota'].mean()
media_amt5 = amostra5['Nota'].mean()
media_amt10 = amostra10['Nota'].mean()
desvio_amt5 = media_pop - media_amt5
desvio_amt10 = media_pop - media_amt10

print(f"Média popular: {media_pop:.2f}")
print(f"Amostra (5): {amostra5}")
print(f"Média amostra (5): {media_amt5:.2f}")
print(f"Amostra (10): {amostra10}")
print(f"Média amostra (10): {media_amt10:.2f}")
print(f"Desvio padrão da amostra (5): {desvio_amt5:.2f}")
print(f"Desvio padrão da amostra (10): {desvio_amt10:.2f}")