"""
1) Crie uma função que receba um número inteiro como parâmetro e verifique se ele é primo ou não,
e exibindo uma mensagem dentro da função.
"""


def verif_primos(n):
    cont = 0
    for i in range(1, n+1):
        if n % i == 0:
            cont += 1
    print(f'O número {n} ', end='')
    if cont == 2:
        print('É PRIMO')
    else:
        print('NÃO É PRIMO')


num = int(input('\nDigite um número inteiro: '))
verif_primos(num)
