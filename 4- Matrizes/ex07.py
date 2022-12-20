from random import randint
#Variáveis
mat = []
primos = []
media_impares = qtd_impares = linha = coluna = 0

#Preenchimento matriz
for i in range(3):
    lin = []
    for j in range(5):
        lin.append(randint(0, 30))
    mat.append(lin)

#Cálculos
maior = mat[0][0]
for i in range(3):
    for j in range(5):
        if mat[i][j] > maior:
            maior = mat[i][j]
            linha = i
            coluna = j
        if mat[i][j] % 2 == 1:
            media_impares += mat[i][j]
            qtd_impares += 1

        cont = 0
        for c in range(1, mat[i][j]+1):
            if mat[i][j] % c == 0:
                cont += 1
        if cont == 2 and mat[i][j] not in primos:
            primos.append(mat[i][j])

if qtd_impares > 0:
    media_impares = media_impares / qtd_impares
primos.sort()

#Prints
print('   ..::Matriz::..')
print('-' * 21)
for i in range(3):
    print('|', end='')
    for j in range(5):
        if i == linha and j == coluna:
            print(f'*{mat[i][j]:2}|', end='')
        else:
            print(f'{mat[i][j]:3}|', end='')
    print()
linha += 1
coluna += 1
print(f'\n◦Maior elemento da matriz: *{maior} -> Linha: {linha} x Coluna: {coluna}')
print(f'◦Média dos números ímpares: {media_impares:.0f}')
print(f'◦Números primos da matriz: {primos}')
