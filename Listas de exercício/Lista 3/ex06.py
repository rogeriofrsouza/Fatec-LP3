"""6) Escreva um programa que leia uma matriz 6 x 10, some as colunas individualmente e acumule as somas na 7ª linha da matriz. O programa deverá mostrar o resultado de cada coluna."""

from random import randint

#Variáveis
mat = []
somas = []
k = 0

#Preenchimento matriz
for i in range(6):
  lin = []
  for j in range(10):
    lin.append(randint(1, 30))
  mat.append(lin)

#Cálculos
for i in range(10):
    soma_col = 0
    for j in range(6):
        soma_col += mat[j][i]
    somas.append(soma_col)

#Prints
print(' ' * 20, '~~Matriz~~', ' ' * 20)
print('-' * 51)

for i in range(8):
    for j in range(10):
        if i < 6:
            print(f'| {mat[i][j]:3}', end='')  

        elif i == 6:
            print('|----', end='')

        elif i > 6:
            print(f'| {somas[k]:3}', end='')
            k += 1
                
    if i <= 6:
        print('|')
    elif i == 7:
        print('|', end='')
        print('  >>Soma colunas<<')

print('-' * 51)
print()
