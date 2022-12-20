from random import randint
matriz = []
soma_linhas = []
for i in range(3):
    lin = []
    for j in range(3):
        lin.append(randint(1, 20))
    matriz.append(lin)

for i in range(3):
    soma = 0
    for j in range(3):
        soma += matriz[i][j]
    soma_linhas.append(soma)

maior = max(soma_linhas)
idx = soma_linhas.index(maior)

print('  +.Matriz.+')
print('=' * 15)
for i in range(3):
    print('|', end='')
    for j in range(3):
        print(f'{matriz[i][j]:3}| ', end='')
    if soma_linhas[i] == maior:
        print(f' *Soma da linha: {soma_linhas[i]}*  >>Maior soma<<')
    else:
        print(f'  Soma da linha: {soma_linhas[i]}')

print(f'\n- Linha de maior soma: {idx+1}')
