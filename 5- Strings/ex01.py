"""Preencha uma lista com 5 nomes de alunos. Em seguida utilize o método upper() para transformar em
letra maiúscula todos os nomes armazenados na lista. Faça uma rotina que procure por nomes nessa lista e
substitua esse nome por outro."""

from time import sleep
nomes = []
res = []
opcao = ''

# Fill array
for i in range(5):
    nomes.append(input(f'{i+1}. Nome aluno(a): ').upper())

# MENU
while opcao != '4':
    print('\n' * 2)
    print('.:ESCOLA JAVALI CANSADO:.')
    print('=' * 25)

    print('\nMENU')
    print('[1] Pesquisar nome')
    print('[2] Lista de nomes cadastrados')
    print('[3] Mudar nome')
    print('[4] Sair')
    opcao = input('Digite sua opção: ')

    # 1
    if opcao == '1':
        nome = input('\nNome a ser pesquisado: ')

        if nome.upper() in nomes:
            print(f'Encontrei: {nome.upper()} :)')
            sleep(3)
        else:
            print('ERRO: nome não registrado :(')
            sleep(3)
    # 2
    elif opcao == '2':
        print(f'\nREGISTRO: ', end='')

        for i in range(5):
            print(f' {i + 1}. {nomes[i]} | ', end='')
        sleep(6)
    # 3
    elif opcao == '3':
        old_name = input('\nQual nome você gostaria de mudar? ')

        if old_name.upper() in nomes:
            new_name = input(f'Qual será o novo nome de {old_name.upper()}? ')

            # words = [w.replace('[br]', '<br />') for w in words]
            nomes = [sub.replace(old_name.upper(), new_name.upper()) for sub in nomes]
            print('\nPronto! Nome atualizado!')
        else:
            print('ERRO: nome não registrado :(')
        sleep(3)
    # 4
    elif opcao == '4':
        break

    else:
        print('\nERRO: Digite uma opção válida')
        sleep(3)

# End
print('\n' * 2)
print('S A I N D O ...\n')
