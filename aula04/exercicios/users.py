import pandas as p
import numpy
from random import shuffle
import matplotlib.pyplot as mpl

so = ['Windows'] * 44 + ['Linux'] * 28  + ['macOS'] * 16 + ['Android'] * 10 + ['iOS'] * 2
shuffle(so)
age = numpy.random.randint(18, 65, 100)
lan = ['Java'] * 15 + ['Python'] * 33 + ['JavaScript'] * 22 + ['C'] * 20 + ['PHP'] * 2 + ['C++'] * 7 + ['Assembly'] * 1
shuffle(lan)
time = numpy.random.randint(1, 16, 100)

users = {
    'Idade': age,
    'SO': so, 
    'Linguagem': lan,
    'Tempo Diario': time
}

users_df = p.DataFrame(users)
print(users_df.head(10))

frequencia_age = users_df['Idade'].value_counts().sort_index()
frequencia_so = users_df['SO'].value_counts().sort_index()
frequencia_lan = users_df['Linguagem'].value_counts().sort_index()
frequencia_time = users_df['Tempo Diario'].value_counts().sort_index()

frequenciaR_age = (frequencia_age / int(len(users_df['Idade']))) * 100
frequenciaR_so = (frequencia_so / int(len(users_df['SO']))) * 100
frequenciaR_lan = (frequencia_lan / int(len(users_df['Linguagem']))) * 100
frequenciaR_time = (frequencia_time / int(len(users_df['Tempo Diario']))) * 100

# freq_so = p.Series(frequenciaR_so)
# freq_so.plot(kind='bar', title='Sistemas Operacionais %')
# mpl.show()

# freq_age = p.Series(frequenciaR_age)
# mpl.hist(users_df['Idade'], bins=20)
# mpl.title('Idades')
# mpl.show()

freq_time = p.Series(frequenciaR_time)
mpl.boxplot(users_df['Tempo Diario'])
mpl.title('Tempo Diario')
mpl.show()
