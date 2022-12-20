"""2) Escreva um programa que preencha uma matriz 4 x 6 com números inteiros, calcule e mostre na tela:
a) A quantidade de números que estão no intervalo entre 10 e 30
b) A soma dos números maiores que 10
c) A soma dos números que estão na quarta coluna da matriz
d) A média dos números da matriz que estão na terceira linha"""

from random import randint

#Variáveis
mat = []
entre_10e30 = []
maior_10 = soma_4col = media_3lin = 0

#Preenchimento matriz
for i in range(4):
  lin = []
  for j in range(6):
    lin.append(randint(1, 30))
  mat.append(lin)

#Cálculos
for i in range(4):
  for j in range(6):
    if 10 < mat[i][j] < 30 and mat[i][j] not in entre_10e30:
      entre_10e30.append(mat[i][j])
    if mat[i][j] > 10:
      maior_10 += mat[i][j]

    if j == 3:
      soma_4col += mat[i][j]
    if i == 2:
      media_3lin += mat[i][j]
media_3lin = media_3lin / 6

#Prints
print('<<Resultado FINAL>>')
print('-' * 21)

for i in range(4):
  for j in range(6):
      print(f'| {mat[i][j]:2}', end='')
  print('|')

print(f'\na) Encontrei {len(entre_10e30)} números no intervalo entre 10 e 30: {entre_10e30}')
print(f'b) Soma dos números maiores que dez: {maior_10}')
print(f'c) Soma dos números que estão na quarta coluna da matriz: {soma_4col}')
print(f'd) Média dos números da matriz que estão na terceira linha: {media_3lin:.1f}\n')
