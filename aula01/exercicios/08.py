import pandas as p
import matplotlib.pyplot as mpl

personagens = {
    'Name': ['Nobara', 'Erza', 'Frieren', 'Killua', 'Maomao', 'Hange', 'Noe', 'Sakura', 'Himawari', 'Yuru'],
    'Anime': ['Jujutsu Kaisen', 'Fairy Tail', 'Frieren', 'HunterXHunter', 'Hitorigoto no Kusuriya', 'Shingeki no Kyojin', 'Vanitas no Carte', 'WindBreaker', 'Boruto', 'Yomi no Tsugai'],
    'Archetype': ['Ocultist', 'Fighter', 'Ocultist', 'Fighter', 'Specialist', 'Specialist', 'Ocultist', 'Fighter', 'Fighter', 'Fighter']
}

df = p.DataFrame(personagens)
mpl.bar(df['Name'], df['Archetype'], color='#11bbdd')
mpl.title('Achetypes - Characters')

print(df)
print(df.head(5))
print(df.describe)
print(df.info)
mpl.show()