import time
polt = []
opcao = c = 1
cont = s = 0
mudou = False
fileira = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

for i in range(41):
    polt.append(i)

while cont < 40 or opcao != 0:
    print('Expresso Fatec Itapetininga')
    print('=' * 30, '\n')

    for i in range(0, 10):
        print(f'{fileira[i]}. | {polt[c]:2}', end='')
        c += 1
        print(f'| {polt[c]:2}|    ', end='')
        c += 1
        print(f'| {polt[c]:2}', end='')
        c += 1
        print(f'| {polt[c]:2}|')
        c += 1

    while mudou == False:
        opcao = int(input('\nDigite o número da poltrona ou zero para sair: '))

        if opcao > 40:
            print('ERRO: Selecione uma poltrone entre 1 e 40.')
            s += 1
            if s > 3:
                break
        elif polt[opcao] == '-':
            print(f'ERRO: Poltrona {opcao} ocupada, tente novamente.')
            s += 1
            if s > 3:
                break
        elif opcao == 0:
            break
        else:
            print(f'Você escolheu a poltrona: {opcao}')
            time.sleep(3)
            polt[opcao] = '-'
            mudou = True

    if opcao == 0:
        print('\nT e r m i n a n d o ...')
        break
    else:
        print('\n' * 10)
        cont += 1
        c = 1
        mudou = False
        s = 0
