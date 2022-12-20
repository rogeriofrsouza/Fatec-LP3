from random import randint
dados = []
cont = [0] * 7

for i in range(10):
    dados.append(randint(1, 6))

for i in range(10):
    cont[dados[i]] += 1

print(dados)
print(cont)

print('\n*Resultado*')
for i in range(1, 7):
    if cont[i] == 0:
        print(f'O nº {i} não foi sorteado.')
    elif cont[i] == 1:
        print(f'O nº {i} foi sorteado apenas 1 vez.')
    else:
        print(f'O nº {i} foi sorteado {cont[i]} vezes.')