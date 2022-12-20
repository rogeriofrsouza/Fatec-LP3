from random import randint
dados = [0] * 7

for i in range(10):
    sort = randint(1, 6)
    dados[sort] += 1

print(dados)

print('\n*Resultado*')
for i in range(1, 7):
    if dados[i] == 0:
        print(f'nº {i} não foi sorteado.')
    elif dados[i] == 1:
        print(f'nº {i} foi sorteado apenas 1 vez.')
    else:
        print(f'nº {i} foi sorteado {dados[i]} vezes.')