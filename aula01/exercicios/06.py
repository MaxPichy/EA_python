import pandas as p
import matplotlib.pyplot as mpl

campeonato = {
    'Time': ['Palmeiras', 'Flamengo', 'Corinthians', 'São Paulo', 'Santos'],
    'Pontos': [48, 46, 41, 38, 35]
}

df = p.DataFrame(campeonato)
mpl.bar(df['Time'], df['Pontos'])
mpl.title('Campeonato')

print(df)
mpl.show()