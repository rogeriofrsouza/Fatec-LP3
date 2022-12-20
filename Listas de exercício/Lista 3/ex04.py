"""4) Escreva um programa que armazene em uma matriz, o nome e duas notas de 5 alunos.
Calcule e armazene em uma lista a média de cada aluno e em outra lista o status (media >= 6, “aprovado”, caso contrário, “reprovado”)
• Faça uma opção para que o usuário possa fazer uma pesquisa por nome. Se encontrar seja exibido na tela:
  - posição em que foi encontrado (índice);
  - nome do aluno;
  - as duas notas e a média;
  - status;"""

#Preenchimento matriz
def preencherMatriz():
  nomes = ('ROGÉRIO', 'PEDRO', 'MARIA', 'JOÃO', 'BRUNA')

  for i in range(5):
    lin = []
    for j in range(3):
      if j == 0:
        lin.append(nomes[i])
      else:
        lin.append(randint(2, 10))
    mat.append(lin)

#Cálculos
def calculos():
  for i in range(5):
    media = 0
    for j in range(1, 3):
        media += mat[i][j]
    media = media / 2
    medias.append(media)
    if media > 6:
      status.append('APROVADO')
    else:
      status.append('REPROVADO')

#Nome pesquisado
def mostrarNome(idx):
  print('\n')
  print('=' * 76)
  
  for i in range(2):
    for j in range(6):
        #Tabela
        if i == 0:
            if j == 0:
                print('|', ' ' * 12, end='')
            elif j == 1:
                print('|', ' ' * 5, 'NOME', ' ' * 4, end='')
            elif j <= 3:
                print(f'|  NOTA {j-1}  ', end='')
            elif j == 4:
                print('|  MÉDIA  ', end='')
            elif j > 4:
                print('|   STATUS  |')

        elif i == 1:
            if j == 0:
                print(f'| {idx+1}. ALUNO(A) |', end='')
        #Valores listas
            elif j == 1:
                print(f' {mat[idx][j-1]:14} |', end='')
            elif j <= 3:
                print(f'     {mat[idx][j-1]:4.1f} |', end='')
            elif j == 4:
                print(f'    {medias[idx]:4.1f} |', end='')
            elif j > 4:
                print(f' {status[idx]:9} |')
  print('=' * 76, '\n')

#Lista Completa
def mostrarLista():  
  k = 0
  print('\n')
  print(' ' * 25, '..::QUADRO FINAL::..', ' ' * 25)
  print('=' * 76)

  for i in range(7):
    for j in range(6):
        #Tabela
        if i == 0:
            if j == 0:
                print('|', ' ' * 12, end='')
            elif j == 1:
                print('|', ' ' * 4, 'NOMES', ' ' * 4, end='')
            elif j <= 3:
                print(f'|  NOTA {j-1}  ', end='')
            elif j == 4:
                print('|  MÉDIA  ', end='')
            elif j > 4:
                print('|   STATUS  |')

        elif i <= 5:
            if j == 0:
                print(f'| {i}. ALUNO(A) |', end='')
        #Valores listas
            elif j == 1:
                print(f' {mat[i-1][j-1]:14} |', end='')
            elif j <= 3:
                print(f'     {mat[i-1][j-1]:4.1f} |', end='')
            elif j == 4:
                print(f'    {medias[k]:4.1f} |', end='')
            elif j > 4:
                print(f' {status[k]:9} |')
                k += 1
  print('=' * 76, '\n')


#Main
from random import randint
import time

mat = []
medias = []
status = []
opcao = 0

preencherMatriz()
calculos()

while opcao != 4:
  print('\n' * 2)
  print('.:FATEC ITAPETININGA:.')
  print('=' * 22)

  print('\nMENU')
  print('[1] Pesquisar nome')
  print('[2] Lista de nomes cadastrados')
  print('[3] Mostrar lista')
  print('[4] Sair')

  opcao = input('Digite sua opção: ')

  if opcao == '1':
    cont = False
    nome = input('\nNome a ser pesquisado: ')

    for i in range(5):
      if nome.upper() == mat[i][0]:
        idx_nome = i
        print('Encontrei :)')
        mostrarNome(idx_nome)
        cont = True
        time.sleep(6)
    if cont == False:
      print('ERRO: nome não registrado!')
      time.sleep(3)

  elif opcao == '2':
    print(f'\nREGISTRO: ', end='')
    for i in range(5):
      if i < 4:
        print(f' {i+1}. {mat[i][0]} | ', end='')
      else:
        print(f' {i+1}. {mat[i][0]} |')
    time.sleep(5)

  elif opcao == '3':
    mostrarLista()
    time.sleep(10)
  
  elif opcao == '4':
    break

  else:
    print('\nERRO: Digite uma opção válida')
    time.sleep(3)

print('\n' * 2)
print('S A I N D O ...\n')
