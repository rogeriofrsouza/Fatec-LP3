"""
1.Crie uma função que receba uma lista X de 10 elementos como parâmetro e retorne a soma dos elementos da lista.
"""
from random import randint  # import sempre no topo do código


def soma():
    s = 0
    for a in range(10):
        s += lista[a]
    return s


# Variáveis
lista = []
for i in range(10):
    lista.append(randint(0, 10))
res = soma()    # Função -> Lista passada por referência

# Prints
cont = 0
print('=' * 21)
for i in range(2):
    for j in range(5):
        print(f'| {lista[cont]:2}', end='')
        cont += 1
    print('|')
print('=' * 21)

print(f'\nSoma dos elementos da lista: {res}')
