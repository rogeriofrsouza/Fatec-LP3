"""1)Escreva um programa que leia uma matriz de ordem 3 x 5 de elementos inteiros, calcule e mostre na tela:
a) menor número da matriz;
b) soma dos números múltiplos de 3 da matriz;
c) média dos números da matriz;"""

from random import randint

#Variáveis
mat = []
mult_3 = media = 0

#Preenchimento matriz
for i in range(3):
  lin = []
  for j in range(5):
    lin.append(randint(1, 20))
  mat.append(lin)

#Cálculos
menor = maior = mat[0][0]
for i in range(3):
  for j in range(5):
    if mat[i][j] < menor:
      menor = mat[i][j]
    if mat[i][j] > maior:
      maior = mat[i][j]
    if mat [i][j] % 3 == 0:
      mult_3 += mat[i][j]
    media += mat[i][j]
media = media / 15

#Prints
print('~~Resultado FINAL~~')
print('-' * 21)

for i in range(3):
  for j in range(5):
    if mat[i][j] == maior or mat[i][j] == menor:
      print(f'|*{mat[i][j]:2}', end='')
    else:
      print(f'| {mat[i][j]:2}', end='')
  print('|')

print(f'\na) Menor número da matriz: {menor}  |  Maior número: {maior}')
print(f'b) Soma dos números múltiplos de três: {mult_3}')
print(f'c) Média dos números da matriz: {media:.1f}')
