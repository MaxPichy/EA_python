# Nosso primeiro DataFrame
import pandas as pd
import matplotlib.pyplot as plt

dados = {
    'Aluno': ['Rogério', 'Matheus', 'Camila', 'Geovanna'],
    'Nota': [8, 5, 9, 6]
}

df = pd.DataFrame(dados)

# df.info() -> mostra infos sobre o array de dados
# print(df.describe()) -> retorna análise dos dados
# print(df.head()) -> organiza os dados em forma de matriz (apenas as primeiras linhas)
# print(df) -> organiza os dados em forma de matriz (todos os dados)

plt.bar(df['Aluno'], df['Nota'])

plt.show()