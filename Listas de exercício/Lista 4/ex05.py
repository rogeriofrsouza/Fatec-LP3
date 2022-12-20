"""5) Escreva uma função que receba como parâmetro uma lista com 10 nomes e um nome para pesquisa. 
Essa função deverá realizar uma busca do nome na lista, retornando TRUE se encontrar ou FALSE se não encontrar."""

from time import sleep


def pesquisar(pesquisa):
    mudou = False
    for elemento in nomes:
        if elemento == pesquisa.upper():
            mudou = True
            return 'Encontrei'
    if not mudou:
        return 'Não encontrei'


# Main
nomes = []
res = False
opcao = '1'

for i in range(10):
    print(f'\n{i+1}.')
    nomes.append(input('NOME: ').upper())


# MENU
while opcao != '3':
    print('\n' * 3)
    print(f'.:SUPER PESQUISA:.')
    print('=' * 18)

    print('\nMENU')
    print('[1] Exibir nomes')
    print('[2] Pesquisar nome')
    print('[3] Sair')
    opcao = input('Digite sua opção: ')

    # 1
    if opcao == '1':
        print('\n' * 2)
        print('=' * 19)
        for i in range(10):
            print(f'|{i+1:2}. {nomes[i]:12} |')
        print('=' * 19)
        sleep(7)
    # 2
    elif opcao == '2':
        pesq = input('\nQual nome você gostaria de pesquisar? ')
        res = pesquisar(pesq)

        print(f'\n{res}: {pesq.upper()}')
        sleep(4)
    # 3
    elif opcao == '3':
        break
    # else
    else:
        print('\nERRO: Digite uma opção válida')
        sleep(4)

# End
print('\n')
print('S A I N D O ...\n')
