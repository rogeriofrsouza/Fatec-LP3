"""
Faça um programa que preencha uma matriz 4 x 4.
A primeira coluna dessa matriz deve armazenar os nomes dos vendedores, as colunas restantes devem armazenas as vendas.
Calcular:
-A média de venda de cada vendedor e armazene em uma lista.
-O total vendido por todos vendedores no trimestre e a maior venda.
-Depois imprima um relatório com o nome do vendedor e a média.
"""
from random import randint

#Variables
mat = []
trimestre = []
medias = []
totais = []
total = k = 0

#Array fill
for i in range(4):
    lin = []
    for j in range(4):
        if j == 0:
            lin.append(input(f'{i+1}. Nome vendedor(a): '))
        else:
            lin.append(randint(800, 4000))
    mat.append(lin)

#Calculations
for i in range(4):
    media = trim = 0
    for j in range(1, 4):
        trim += (mat[i][j])
        media += (mat[i][j])
    trimestre.append(trim)
    media = media / 3
    medias.append(media)

c = 1
for a in range(3):
    tot_col = 0
    for b in range(4):
        tot_col += mat[b][c]
    totais.append(tot_col)
    c += 1
totais.append(sum(trimestre))
totais.append(sum(medias))
maior = max(medias)
menor = min(medias)

#Prints
print('\n' * 5)
print(' ' * 38, '..::RELATÓRIO FINAL::..', ' ' * 38)
print('=' * 100)

for i in range(7):
    for j in range(7):
        #Grid
        if i == 0:
            if j == 0:
                print('|', ' ' * 15, end='')
            elif j == 1:
                print('|', ' ' * 4, 'NOMES', ' ' * 4, end='')
            elif j <= 4:
                print(f'|    MÊS {j-1}   ', end='')
            elif j == 5:
                print('|  TRIMESTRE ', end='')
            elif j == 6:
                print('|    MÉDIA   |')

        elif 0 < i < 5:
            if j == 0:
                print(f'| {i}. VENDEDOR(A) |', end='')
        #Array values
            elif j == 1:
                print(f' {mat[i-1][j-1]:14} |', end='')
            elif j <= 4:
                print(f' R${mat[i-1][j-1]:8.2f} |', end='')
            elif j == 5:
                print(f' R${trimestre[k]:8.2f} |', end='')
            elif j == 6:
                if medias[k] == maior:
                    print(f'+R${medias[k]:8.2f}+|   +MAIOR MÉDIA+')
                elif medias[k] == menor:
                    print(f'-R${medias[k]:8.2f}-|   -menor média-')
                else:
                    print(f' R${medias[k]:8.2f} |')
                k += 1
        elif i == 5:
            if j == 0:
                print('|', ' ' * 14, '|', ' ' * 15, end='')
                print('|', ' ' * 10, '|', ' ' * 10, '|', ' ' * 10, '|', ' ' * 10, '|', ' ' * 10, '|')
        #Total columns
        elif i == 6:
            if j == 0:
                print('| 5. TOTAL ', ' ' * 5, end='')
            elif j == 1:
                print('|', ' ' * 14, '|', end='')
            elif j <= 4:
                print(f' R${totais[j-2]:8.2f} |', end='')
            elif j == 5:
                print(f' R${totais[j-2]:8.2f} |', end='')
            elif j == 6:
                print(f' R${totais[j-2]:8.2f} |')

print('=' * 100)
print()
