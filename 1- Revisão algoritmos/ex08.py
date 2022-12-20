opcao = 'S'

while opcao == 's' or opcao == 'S':
    print('*VERIFICADOR DE DIVISÃO 3 E 5*')
    print('---------===========-----------\n')
    num = int(input('Digite o número para verificar: '))

    if num % 3 == 0 and num % 5 == 0:
        print(f'\nO número {num} é divisível por 3 e 5 :)')
    else:
        print(f'\nO número {num} não é divisível por 3 e 5 :(')

    opcao = str(input('Quer continuar? [S/N]\n'))

print('T E R M I N A N D O...')