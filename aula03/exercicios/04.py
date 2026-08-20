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

mod_df = df[df['Modalidade'] == 'Presencial'].count() 
mod_df2 = df[df['Modalidade'] == 'Remoto'].count()
mod_am = amostra[amostra['Modalidade'] == 'Presencial'].count()
mod_am2 = amostra[amostra['Modalidade'] == 'Remoto'].count()


print(f"População: P = {mod_df}, R = {mod_df2}")
print(f"Amostra: P = {mod_am}, R = {mod_am2}")