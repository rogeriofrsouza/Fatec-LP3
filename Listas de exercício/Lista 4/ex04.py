"""4) Escreva uma função que receba como parâmetro a nota de um estudante, converte o valor de nota para um conceito (A, B, C, D, E e F). 
Imprima o resultado dentro da função."""


def titulo():
  print('\n' * 5)
  print(f'FATEC Itapetininga - ADS 2º ciclo')
  print(f'Aluno(a): {nome}\n')


def converte_notas():
  for i in range(6):
    if 9 < notas[i] <= 10:
      conceitos.append('A')
      situacao.append('Aprovado')
    elif 8 < notas[i] <= 9:
      conceitos.append('B')
      situacao.append('Aprovado')
    elif 7 <= notas[i] <= 8:
      conceitos.append('C')
      situacao.append('Aprovado')
    elif 6 < notas[i] < 7:
      conceitos.append('D')
      situacao.append('Recuperação')
    elif 5 <= notas[i] <= 6:
      conceitos.append('E')
      situacao.append('Recuperação')
    elif notas[i] < 5:
      conceitos.append('F')
      situacao.append('Reprovado')
    else:
      conceitos.append('-')
      situacao.append('Erro :(')


def resultados():
  print('=' * 66)
  print('|           MATÉRIAS         |  NOTAS  |  CONCEITO |  RESULTADO  |')
  print('-' * 66)
  print(f'|1. Sistemas de Informação   |   {notas[0]:4.1f}  |     {conceitos[0]}     | {situacao[0]:11} |')
  print(f'|2. Cálculo                  |   {notas[1]:4.1f}  |     {conceitos[1]}     | {situacao[1]:11} |')
  print(f'|3. Engenharia de Software I |   {notas[2]:4.1f}  |     {conceitos[2]}     | {situacao[2]:11} |')
  print(f'|4. Linguagem de Programação |   {notas[3]:4.1f}  |     {conceitos[3]}     | {situacao[3]:11} |')
  print(f'|5. Comunicação e Expressão  |   {notas[4]:4.1f}  |     {conceitos[4]}     | {situacao[4]:11} |')
  print(f'|6. Contabilidade            |   {notas[5]:4.1f}  |     {conceitos[5]}     | {situacao[5]:11} |')
  print('=' * 66)
  print('\n')


# Main
notas = []
conceitos = []
situacao = []

print('\nFATEC Itapetininga - ADS 2º ciclo')
print('-' * 33)
nome = input('\nQual o seu nome? ')
print(f'Olá {nome}, digite suas notas de:')

notas.append(float(input('\n1. Sistemas de Informação: ')))
notas.append(float(input('2. Cálculo: ')))
notas.append(float(input('3. Engenharia de Software I: ')))
notas.append(float(input('4. Linguagem de Programação: ')))
notas.append(float(input('5. Comunicação e Expressão: ')))
notas.append(float(input('6. Contabilidade: ')))

converte_notas()
titulo()
resultados()
