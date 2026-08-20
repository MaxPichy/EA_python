import random

alunos = ['Rogério', 'Ricardo', 'Shimada', 'Caio', 'Camila', 'Vitor', 'Geovanna', 'Renan', 'Carlos', 'Miguel', 'Ana', 'Sthevens', 'Guilherme', 'Raissa', 'Matheus', 'Felipe', 'Endrew', 'Arthur', 'Gabriela', 'Pedro']

random.seed(15)

amostra = random.sample(alunos, 4)
print(amostra)