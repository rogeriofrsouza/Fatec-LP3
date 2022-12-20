from random import randint
matriz = []
media = maior_media = 0

for i in range(3):
    linhas = []
    for j in range(4):
        linhas.append(randint(0, 30))
        media += linhas[j]
    matriz.append(linhas)

media = media / 12

for i in range(3):
    for j in range(4):
        if matriz[i][j] > media:
            maior_media += 1

for i in range(3):
    print(f'{matriz[i]}')

print('\n+..-..+Resultado Final+..-..+')
print('=' * 30)

print(f'Média de todos elementos: {media:.1f}')
print(f'Quantidade de elementos maiores que a média: {maior_media}')
