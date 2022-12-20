"""
3. Crie uma função que receba dois números inteiros por parâmetro e retorne a soma dos
N números inteiros existentes entre esses dois números (imprima o resultado no programa principal)
"""


def contar(x, y):
    soma_numeros = 0
    if x < y:
        for i in range(x, y+1):
            soma_numeros += i
    elif x > y:
        for i in range(x, y-1, -1):
            soma_numeros += i
    return soma_numeros


# Main
opcao = ''
pular = False
while opcao.upper() != 'N':
    if pular:
        print('\n' * 10)
    n1 = int(input('\nEscolha um número inteiro: '))
    n2 = int(input('Escolha outro nº inteiro: '))

    soma = contar(n1, n2)
    if soma != 0:
        print(f'\nA soma dos N números inteiros entre {n1} e {n2} é: {soma}')
    else:
        print('\nERRO: escolha dois números inteiros diferentes!')

    opcao = input('\nGostaria de continuar? [S/N]\n')
    pular = True

print('\n' * 3)
print('T E R M I N A N D O ...')
