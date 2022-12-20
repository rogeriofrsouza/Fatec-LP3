"""
4) Faça um programa que solicita as notas das duas provas feitas por cada um dos 5 alunos de uma turma,
e imprime para cada um a média das notas. A média deve ser feita usando uma função que recebe as duas notas
e retorna a média.
"""
# Variáveis
from random import randint
alunos = []
nota1 = []
nota2 = []
medias = []


def media(n1, n2):
    m = (n1 + n2) / 2
    return m


# Cálculos
for i in range(5):
    print(f'\nAluno(a) {i+1}')
    alunos.append(input('NOME: '))
    nota1.append(randint(30, 100) / 10)
    nota2.append(randint(30, 100) / 10)

    res = media(nota1[i], nota2[i])
    medias.append(res)

# Prints
print()
print(' ' * 13, 'FATEC Itapetininga', ' ' * 13)
print('=' * 44)

for i in range(6):
    for j in range(4):
        if i == 0:
            if j == 0:
                print('|', ' ' * 4, 'NOMES', ' ' * 4, end='')
            elif j < 3:
                print(f'| NOTA {j} ', end='')
            else:
                print(f'| MÉDIA |')

        elif i > 0:
            if j == 0:
                if len(alunos[i-1]) <= 14:
                    print(f'| {alunos[i-1]:14} ', end='')
                else:
                    print(f'|', '-' * 14, '', end='')
            elif j == 1:
                print(f'|   {nota1[i-1]:3.1f}  ', end='')
            elif j == 2:
                print(f'|   {nota2[i-1]:3.1f}  ', end='')
            else:
                print(f'|  {medias[i-1]:3.1f}  |')
print('=' * 44)
print('\n')


