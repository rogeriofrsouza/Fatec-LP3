from random import randint
matriz = []
pares = impares = 0

for i in range(2):
    linha = []
    for j in range(4):
        linha.append(randint(0, 20))
    matriz.append(linha)

for c in range(2):
    print(f'{matriz[c]}')

for i in range(2):
    for j in range(4):
        if matriz[i][j] % 2 == 0:
            pares += 1
        else:
            impares += matriz[i][j]

print('\n\_*Resultado Final*_/')
print('======================')
print(f'Quantidade de elementos pares: {pares}')
print(f'Soma dos elementos ímpares: {impares}')
