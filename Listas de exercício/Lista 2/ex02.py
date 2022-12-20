cores = ['AZUL', 'VERMELHO', 'PRETO', 'BRANCO', 'AMARELO', 'VERDE', 'ROXO', 'LARANJA', 'MARROM', 'CINZA']
cores2 = []
opcao = 1
print('Olá! Seja muito bem-vindo(a)!')
print('=' * 29)

#MENU
def menu():
    print('\nMENU')
    print('1- Pesquisar no catálogo')
    print('2- Exibir lista de cores disponíveis')
    print('3- SAIR')
    op = input('Digite sua opção: ')
    print('\n' * 2)
    return op

#Análise de opções
while opcao != '3':
    opcao = menu()
    if opcao == '1':
        mudou = False
        while mudou == False:
            c = input('Digite uma cor: ')
            cor = c.upper()
            if cor in cores:
                print(f'{cor} foi encontrado :)')
                if cor in cores2:
                    break
                else:
                    cores2.append(cor)
                mudou = True
            else:
                print(f'{cor.upper()} não foi encontrado :(\n')
                mudou = False
            a = input('\n0- Voltar ao MENU...')
            print('\n' * 3)
    elif opcao == '2':
        c = 1
        print('_.-+Lista+-._ ')
        for i in range(10):
            if cores[i] in cores2:
                print(f'{c:3}. *{cores[i]:7}')
            else:
                print(f'{c:3}.  {cores[i]:8}')
            c += 1
        print(f'Sua pesquisa: ', end='')
        for i in range(len(cores2)):
            print(f'{cores2[i]}|  ', end='')
        print()
        a = input('\n0- Voltar ao MENU...')
        print('\n' * 3)
    elif opcao == '3':
        break
    else:
        print('ERRO: Digite um número válido!')
print('\nSAINDO ...')
