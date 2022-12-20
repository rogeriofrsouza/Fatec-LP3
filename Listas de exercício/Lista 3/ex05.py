"""5) Escreva um programa que preencha uma matriz 4 x 3 com números inteiros, calcule e mostre na tela:
a) A soma dos elementos que estão na 2ª e 4ª linha da matriz
b) A soma dos números primos"""

from random import randint

#Variáveis
mat = []
somas = []
soma_primos = 0

#Preenchimento matriz
for i in range(4):
  lin = []
  for j in range(3):
    lin.append(randint(1, 20))
  mat.append(lin)

#Cálculos
for i in range(4):
    soma_lin = 0
    for j in range(3):
        cont = 0
        for k in range(1, mat[i][j]+1):
            if mat[i][j] % k == 0:
                cont += 1
        if cont == 2:
            soma_primos += mat[i][j]        
        soma_lin += mat[i][j]
    somas.append(soma_lin)

#Prints
print(' ~~Matriz~~ ')
print('-' * 13)

for i in range(4):
  for j in range(3):
    print(f'| {mat[i][j]:2}', end='')
  print(f'|  >>Soma linha: {somas[i]:2}<<')

print(f'\n- Soma dos números primos: {soma_primos}\n')
