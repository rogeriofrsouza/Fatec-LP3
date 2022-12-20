"""3) Um time de basquete possui 12 jogadores. Faça um programa que preencha uma matriz com o nome e a altura dos jogadores, e através de uma função faça os seguintes cálculos:
a) O nome e a altura do jogador mais alto.
b) A média de altura do time.
Obs: A função deverá receber por parâmetro a matriz e imprimir os resultados dentro da função."""

from random import randint

def titulo():
  print('\n' * 5)
  print('TIME JAVALI CANSADO')
  print('-' * 19)


def jogador_mais_alto():
  maior_alt = mat[0][1]

  for i in range(12):
    if mat[i][1] > maior_alt:
      maior_alt = mat[i][1]
      maior_nome = mat[i][0]

  print('\na) Jogador mais alto')
  print(f'NOME: {maior_nome}  | ALTURA: {maior_alt} m')


def media_time():
  media = 0
  for i in range(12):
    media += mat[i][1]

  media = media / 12
  print(f'\nb) Média de altura do time: {media:.2f} m\n')


# Main
mat = []
titulo()

for i in range(12):
  lin = []
  print(f'\nJogador {i+1}')

  lin.append(input('NOME: '))
  lin.append(randint(170, 220) / 100)
  mat.append(lin)

titulo()
jogador_mais_alto()
media_time()
