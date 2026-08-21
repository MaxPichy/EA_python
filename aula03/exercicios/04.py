import pandas as p
from random import shuffle

tipos = ['Presencial'] * 70 + ['Remoto'] * 30
shuffle(tipos)

escola = {
    'Modalidade': tipos,
    'Aluno': ['Korra', 'Toph', 'Kiyoshi', 'Aang', 'Zuko', 'Katara', 'Azula', 'Iroh', 'Vaatu', 'Raava', 'Ko', 'Sokka', 'Maomao', 'Jinshi', 'Jade', 'Erza', 'Bahal', 'Natsu', 'Grey', 'Kenshi', 'Itadori', 'Nobara', 'Gokuyou', 'Tania', 'Yuru', 'Edward', 'Alphonse', 'Winry', 'Lakan', 'Levi', 'Himmel', 'Fern', 'Frieren', 'Soifon', 'Ichigo', 'Megumi', 'Yuta', 'Maki', 'Asa', 'Hohenheim', 'Huges', 'Mustang', 'Hawkaye', 'Izumi', 'Armstrong', 'Xing', 'Inousuke', 'Urokodaki', 'Noé', 'Vanitas', 'Korra', 'Toph', 'Kiyoshi', 'Aang', 'Zuko', 'Katara', 'Azula', 'Iroh', 'Vaatu', 'Raava', 'Ko', 'Sokka', 'Maomao', 'Jinshi', 'Jade', 'Erza', 'Bahal', 'Natsu', 'Grey', 'Kenshi', 'Itadori', 'Nobara', 'Gokuyou', 'Tania', 'Yuru', 'Edward', 'Alphonse', 'Winry', 'Lakan', 'Levi', 'Himmel', 'Fern', 'Frieren', 'Soifon', 'Ichigo', 'Megumi', 'Yuta', 'Maki', 'Asa', 'Hohenheim', 'Huges', 'Mustang', 'Hawkaye', 'Izumi', 'Armstrong', 'Xing', 'Inousuke', 'Urokodaki', 'Noé', 'Vanitas']
}

df = p.DataFrame(escola)
amostra = df[df['Modalidade'] == 'Presencial']

pop_al = df['Aluno'].count()
am_al = amostra['Aluno'].count()

pop_p = (df['Modalidade'] == 'Presencial').sum()
pop_r = (df['Modalidade'] == 'Remoto').sum()
am_p = (amostra['Modalidade'] == 'Presencial').sum()
am_r = (amostra['Modalidade'] == 'Remoto').sum()

print(f'Quantidade de alunos (população): {pop_al}')
print(f'Composição por modalidade de alunos (população): Presencial {pop_p}, Remoto {pop_r}')
print(f'Quantidade de alunos (amostra): {am_al}')
print(f'Composição por modalidade de alunos (população): Presencial {am_p}, Remoto {am_r}')
print('Essa amostra não representa a população, ela possui um viés baseado na modalidade do curso.')