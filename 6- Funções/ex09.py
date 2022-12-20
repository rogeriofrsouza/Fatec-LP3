"""
2) Crie um programa que o usuário escolha através de opções, o cálculo que desejar realizar.
1- Verifica se o número é primo;
2– Verifica se o número é perfeito;
3– Calcula o fatorial do número.

- Para cada cálculo deve ser criado uma função que recebe como parâmetro o número e retorna o resultado.
- Número perfeito => a soma dos seus divisores exceto ele mesmo é o próprio número.
"""
from time import sleep
from random import randint


def primos(num):
    for a in range(2, num):
        if num % a == 0:
            return 'NÃO é PRIMO.'

    return 'é PRIMO.'


def perfeitos(num):
    soma = 0
    for b in range(1, num):
        if num % b == 0:
            soma += b

    if soma == num:
        return 'é PERFEITO.'
    else:
        return 'NÃO é PERFEITO.'


def fatorial(num):
    fat = 1
    for c in range(1, num+1):
        fat = fat * c
    return fat


# Main
opcao = '1'
numero = randint(2, 10)

# MENU
while opcao != '5':
    print('\n' * 3)
    print(f'.:SUPER CALCULADORA:.')
    print('=' * 21)

    print('\nMENU')
    print(f'[1] Modificar número: [{numero}]')
    print(f'[2] Verificar se {numero} é PRIMO')
    print(f'[3] Verificar se {numero} é PERFEITO')
    print(f'[4] Calcular o FATORIAL de {numero}')
    print('[5] SAIR')
    opcao = input('Digite sua opção: ')

    # 1
    if opcao == '1':
        mudou = False
        while not mudou:
            numero = int(input('\nDigite um número inteiro positivo: '))
            if numero > 0:
                mudou = True
                print(f'[Alteração concluída]')
                sleep(2)
    # 2
    elif opcao == '2':
        res_primo = primos(numero)

        print(f'\n{numero} {res_primo}')
        sleep(4)
    # 3
    elif opcao == '3':
        res_perfeito = perfeitos(numero)

        print(f'\n{numero} {res_perfeito}')
        sleep(4)
    # 4
    elif opcao == '4':
        res_fatorial = fatorial(numero)

        print(f'\nFatorial: {numero}! = {res_fatorial}')
        sleep(4)
    # 5
    elif opcao == '5':
        break
    # else
    else:
        print('\nERRO: Digite uma opção válida')
        sleep(4)

# End
print('\nS A I N D O ...')
