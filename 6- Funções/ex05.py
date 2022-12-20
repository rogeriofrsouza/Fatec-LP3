"""
5) Escreva uma função com o nome soma_quadrados que recebe um número inteiro positivo n,
e tem como retorno a soma do quadrado de todos os números até n.
"""
from time import sleep
n = 0


def menu():
    print('\n²Calculadora de Quadrados²')
    print('|_|' * 9, '\n')


def soma_quadrados(num):
    soma = 0
    for j in range(0, num+1):
        soma = soma + (pow(j, 2))
    return soma


menu()
print('REGRAS:')
print('-Escolha um número inteiro positivo.')
print('-Somarei o quadrado de cada nº positivo, partindo do zero (0) até chegar nele: ')

while n <= 0:
    n = int(input('\nDigite a sua escolha: '))
print('\nA G U A R D E ', end='')

for i in range(3):
    sleep(1)
    print('. ', end='')

sleep(1)
res = soma_quadrados(n)

print('\n' * 5)
menu()
print(f'-Número escolhido: {n}')
print(f'-Resultado final: {res}')
