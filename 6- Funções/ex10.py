"""3.Faça um programa que preencha uma matriz de ordem 3 x 3 de elementos inteiros.
Faça uma função para cada cálculo abaixo:

-A quantidade de números pares da matriz;
-A soma dos elementos diagonal principal da matriz;
-A média dos elementos da matriz;
Obs: os resultados deverão ser impressos no programa principal."""

from random import randint


def calc_pares():
    qtd_pares = 0
    for a in range(3):
        for b in range(3):
            if mat[a][b] % 2 == 0:
                qtd_pares += 1
                if mat[a][b] not in pares:
                    pares.append(mat[a][b])
    return qtd_pares


def diag_principal():
    soma_diag = 0
    for a in range(3):
        for b in range(3):
            if a == b:
                soma_diag += mat[a][b]
    return soma_diag


def calc_media():
    media = 0
    for a in range(3):
        for b in range(3):
            media += mat[a][b]
    media = media / 9
    return media


# Main
mat = []
pares = []

# Fill array
for i in range(3):
    lin = []
    for j in range(3):
        lin.append(randint(0, 15))
    mat.append(lin)

# Calculations
res_pares = calc_pares()
res_diag = diag_principal()
res_media = calc_media()

# Prints
print('\n .:Matriz:. ')
print('=' * 13)

for i in range(3):
    for j in range(3):
        print(f'| {mat[i][j]:2}', end='')
    print('|')
print('=' * 13)

print(f'\n-Encontrei {res_pares} números pares na matriz: {sorted(pares)}')
print(f'-Soma dos elementos da diagonal principal: {res_diag}')
print(f'-Média dos elementos da matriz: {res_media:.1f}')
