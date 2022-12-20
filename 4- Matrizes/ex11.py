"""Faça um programa que leia uma matriz 5x2 com os números de telefones dos clientes.
As linhas representam os clientes, as colunas representam os telefones.
Em seguida, faça uma lista de 5 elementos com os nomes dos clientes.
Depois de preenchidos a lista e a matriz, se o nome existir, deverá ser mostrado na tela, os telefones desse cliente"""


# Search name
def mostrarNome(idx):
    print('\n')
    print('=' * 42)

    for i in range(2):
        for j in range(4):
            # Tabela
            if i == 0:
                if j == 0:
                    print('|', ' ' * 12, '|', end='')
                elif j <= 2:
                    print(f' TELEFONE {j} |', end='')
                else:
                    print()
            else:
                if j == 0:
                    print(f'| {nomes[idx]:12} |', end='')
                elif j == 1:
                    print(f'  {telefones[idx][j-1]:9} |', end='')
                elif j == 2:
                    print(f'  {telefones[idx][j-1]:8}  |', end='')
                else:
                    print()
    print('=' * 42, '\n')


# Complete list
def mostrarLista():
    print('\n')
    print(' ' * 10, '..::LISTA COMPLETA::..', ' ' * 10)
    print('=' * 46)

    for i in range(6):
        for j in range(4):
            # Tabela
            if i == 0:
                if j == 0:
                    print('|', ' ' * 16, '|', end='')
                elif j <= 2:
                    print(f' TELEFONE {j} |', end='')
                else:
                    print()
            else:
                if j == 0:
                    print(f'| {i}. {nomes[i-1]:13} |', end='')
                elif j == 1:
                    print(f'  {telefones[i-1][j-1]:9} |', end='')
                elif j == 2:
                    print(f'  {telefones[i-1][j-1]:8}  |', end='')
                else:
                    print()
    print('=' * 46, '\n')


# Main
from random import randint
import time

telefones = []
nomes = []
opcao = ''

# Array fill
for i in range(5):
    linha = []
    linha.append(randint(990000000, 999999999))
    linha.append(randint(32000000, 32999999))
    telefones.append(linha)

print('.:CADASTRO DE CLIENTES::.')
print('=' * 25)
for k in range(5):
    nomes.append(input(f'{k+1}. NOME: ').upper())

# MENU
while opcao != '4':
    print('\n' * 2)
    print('.:TELEFONIA FATECANOS:.')
    print('=' * 23)

    print('\nMENU')
    print('[1] Pesquisar nome')
    print('[2] Lista de nomes cadastrados')
    print('[3] Mostrar lista')
    print('[4] Sair')

    opcao = input('Digite sua opção: ')
    # 1
    if opcao == '1':
        cont = False
        nome = input('\nNome a ser pesquisado: ')

        for i in range(5):
            if nome.upper() == nomes[i]:
                idx_nome = i
                print('Encontrei :)')
                mostrarNome(idx_nome)
                cont = True
                time.sleep(6)
        if cont == False:
            print('ERRO: nome não registrado!')
            time.sleep(3)
    # 2
    elif opcao == '2':
        print(f'\nREGISTRO: ', end='')
        for i in range(5):
            print(f' {i + 1}. {nomes[i]} | ', end='')
        time.sleep(5)
    # 3
    elif opcao == '3':
        mostrarLista()
        time.sleep(12)
    # 4
    elif opcao == '4':
        break

    else:
        print('\nERRO: Digite uma opção válida')
        time.sleep(3)

# End
print('\n' * 2)
print('S A I N D O ...\n')
