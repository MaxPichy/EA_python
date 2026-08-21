import pandas as p

cursos = {
    'Curso': ['DSM', 'Processos Gerenciais', 'Gestão Empresarial'],
    'Alunos': [500, 300, 200]
}

df = p.DataFrame(cursos)

total_pop = df['Alunos'].sum()
df['Amostra-100'] = (df['Alunos'] / total_pop) * 100 

print(f'Quantidade ideal de alunos na amostra por curso: \n{df[['Curso', 'Amostra-100']]}.')