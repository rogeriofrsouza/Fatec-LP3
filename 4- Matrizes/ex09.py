"""
Faça um programa que preencha uma matriz 5 x 4. A primeira coluna dessa matriz deve
armazenar os nomes dos alunos, as colunas restantes devem armazenar as notas de cada aluno.
Calcule:
-A média de cada aluno e armazene em uma lista;
-Depois imprima um relatório com o nome do aluno e a média.
"""
from random import randint

#Variables
mat = []
medias = []
cont = 1
k = -1

#Array fill
for i in range(5):
    lin = []
    for j in range(4):
        if j == 0:
            lin.append(input(f'Nome do(a) aluno(a) {cont}: '))
        else:
            lin.append(randint(4, 10))
    mat.append(lin)
    cont += 1

#Calculations
for i in range(5):
    media = 0
    for j in range(4):
        if j > 0:
            media += mat[i][j]
    media = media / 3
    medias.append(media)

#Prints
print('\n' * 5)
print(' ' * 20, '..::RELATÓRIO FINAL::..', ' ' * 21)
print('=' * 64)

for i in range(6):
    for j in range(6):
        #Grid
        if i == 0:
            if j == 0:
                print('|', ' ' * 12, end='')
            elif j == 1:
                print('|    NOMES    |', end='')
            elif j <= 4:
                print(f' NOTA {j-1} |', end='')
            elif j == 5:
                print(f' MÉDIA |')

        elif i > 0:
            if j == 0:
                print(f'| {i}. ALUNO(A) |', end='')
        #Array values
            elif j == 1:
                print(f' {mat[i-1][j-1]:11} |', end='')
            elif j <= 4:
                print(f' {mat[i-1][j-1]:6} |', end='')
            elif j == 5:
                print(f' {medias[k]:5.1f} |')
                k += 1
print()
