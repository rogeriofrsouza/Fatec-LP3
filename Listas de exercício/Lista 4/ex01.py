"""1) Crie uma função que receba 1 número inteiro como parâmetro e verifique se ele é perfeito, ou seja, 
se a soma dos seus divisores exceto ele mesmo dá o próprio número, a mensagem se o número é perfeito ou não 
deve ser mostrada no programa principal."""

def verif_perfeito(n):
  cont = 0
  for i in range(1, n):
    if n % i == 0:
      cont += i
  
  if cont == num:
    return 'é PERFEITO :)'
  else:
    return 'NÃO é PERFEITO :('


# Main
opcao = 'S'

while opcao.upper() != 'N':
  print('\n' * 5)
  print('.:Verificador de Perfeitos:.')
  print('-' * 28)

  num = int(input('\nDigite um número para verificar: '))
  res = verif_perfeito(num)

  print(f'{num} {res}')
  opcao = input('\nGostaria de continuar? [S/N]\n')

print('\nTerminando . . .')
