"""
2. Crie uma função que gere e mostre os dez primeiros números pares acima de 100
"""


def pares_100(n):
    qtd_pares = 0
    if n < 100:
        for i in range(n, 100+1):
            if i % 2 == 0:
                pares.append(i)
                qtd_pares += 1
    elif n > 100:
        for i in range(n, 100-1, -1):
            if i % 2 == 0:
                pares.append(i)
                qtd_pares += 1
    return qtd_pares


# Main
from time import sleep
opcao = ''
num = int(input('\nEscolha um número para contagem de pares até o 100: '))

# MENU
while opcao != '3':
    pares = []
    print('\n' * 2)
    print(f'.:SUPER CONTADORA ({num}):.')
    print('=' * 22 + '=' * len(str(num)))

    print('\nMENU')
    print('[1] Exibir pares')
    print('[2] Mudar de número')
    print('[3] Sair')
    opcao = input('Digite sua opção: ')

    # 1
    if opcao == '1':
        qtd = pares_100(num)

        if qtd > 1:
            print(f'\nDo número {num} ao 100, foram encontrados {qtd} números pares: \n{pares}')
        elif qtd == 1:
            print(f'\nDo número {num} ao 100, foi encontrado apenas {qtd} número par: \n{pares}')
        else:
            print('\nNão foi encontrado nenhum número par :(')
        sleep(7)
    # 2
    elif opcao == '2':
        number = int(input('\nPara qual número você gostaria de mudar? '))

        if number != num:
            print('Pronto! Número atualizado!')
            num = number
        else:
            print('ERRO: Tente novamente!')
        sleep(3)
    # 3
    elif opcao == '3':
        break
    # else
    else:
        print('\nERRO: Digite uma opção válida')
        sleep(3)

# End
print('\n')
print('S A I N D O ...\n')
