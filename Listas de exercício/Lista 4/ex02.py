"""2) Crie uma função que receba três valores, 'a', 'b' e 'c', que são os coeficientes de uma equação do segundo grau e 
retorne o valor do delta, que é dado por 'b² - 4ac’."""

from math import sqrt


def calc_delta(n1, n2, n3):
  res_delta = pow(n2, 2) - (4 * n1 * n3)
  return res_delta


def calc_equacao_2grau(n1, n2, d):
  solucao[0] = (-n2 + sqrt(d)) / (2 * n1)
  solucao[1] = (-n2 - sqrt(d)) / (2 * n1)
  solucao.sort()


# Main
solucao = [0] * 2
opcao = 'S'

while opcao.upper() != 'N':
  print('\n' * 5)
  print('Calculadora - Equação 2º grau')
  print('-' * 29)

  a = int(input('\nDigite o valor de a: '))
  b = int(input('Digite o valor de b: '))
  c = int(input('Digite o valor de c: '))

  delta = calc_delta(a, b, c)
  calc_equacao_2grau(a, b, delta)
  
  print(f'\nDELTA = {delta}')
  for i in range(2):
    if i == 0:
      print('Solução = {', end='')
      print(f'{solucao[i]:.0f}, ', end='')
    else:
      print(f'{solucao[i]:.0f}', end='')
      print('}')

  opcao = input('\nGostaria de continuar? [S/N]\n')

print('\nAté mais! . . .')
