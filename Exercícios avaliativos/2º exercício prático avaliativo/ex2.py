"""
    Exercício avaliativo do 2º bimestre–Matutino

    Escreva um programa em Python que preencha uma matriz de ordem 5 x 5 com números inteiros e mostre na tela a matriz preenchida. (2pts)
    Calcule e mostre na tela:
    •A média dos números múltiplos de 3 (1,5 pts);
    •O menor número da coluna 3, ou seja, índice 2 (1,5 pts);
    •A média dos números da 5ª linha da matriz, ou seja, índice 4 (1,5 pts);
    •A quantidade de números da matriz que são ímpares, e maiores ou iguais a 10 e menores ou iguais a 15 (1,5 pts);
    •Faça a média dos números de cada linha da matriz e armazene em uma lista.(2 pts)
"""

#Variáveis
from random import randint
mat = []
media_lin = []
mult3 = []
menor_col3 = imp_entre10e15 = 0

#Preenchimento matriz
for i in range(5):
    lin = []
    for j in range(5):
        lin.append(randint(0, 30))
    mat.append(lin)
    media_lin.append(sum(lin) / len(lin))

#Cálculos
menor_col3 = mat[0][2]
for i in range(5):
    for j in range(5):
        if mat[i][j] % 3 == 0 and mat[i][j] != 0:
            mult3.append(mat[i][j])
        if mat[i][2] < menor_col3:
            menor_col3 = mat[i][2]
        if mat[i][j] % 2 == 1 and 10 <= mat[i][j] <= 15:
            imp_entre10e15 += 1

#Prints
print('\n+FATEC  Itapetininga+')
print('-' * 21)

for i in range(5):
    print('+---+---+---+---+---+')
    for j in range(5):
        print(f'| {mat[i][j]:2}', end='')
    print(f'|   *Média linha {i+1}: {media_lin[i]:3.1f}')
print('+---+---+---+---+---+')

print(f'\n•Números múltiplos de três: {mult3}  |  Média: {sum(mult3) / len(mult3):.1f}')
print(f'•Menor número da coluna três: {menor_col3}')
print(f'•Quantidade de números da matriz que são ímpares, e maiores ou iguais a dez e menores ou iguais a quinze: {imp_entre10e15}\n')
