import pandas as p

alunos = {
    'Nome': ['Alicia', 'Manuela', 'Iris', 'Mulan', 'Heidi', 'Jamile', 'Yasmin', 'Luana', 'Gabriel', 'Kamilly','Sammuel', 'Dean', 'Rose', 'John', 'Vânia', 'Marcos', 'Gustavo', 'Emily', 'Bonifácio', 'Joana'],
    'Idade': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
    'Nota': [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
}

df = p.DataFrame(alunos)

print(df)
print(df.head(5))
print(df.describe)
print(df.info)