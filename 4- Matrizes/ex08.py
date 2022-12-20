from random import randint
#Variáveis
mat = []
maiores = []
maior_media = media = 0
mostra = mostra2 = False

#Preenchimento matriz
for i in range(5):
    lin = []
    for j in range(5):
        lin.append(randint(0, 30))
    media += sum(lin)
    mat.append(lin)

#Cálculos
media = media / 25
maior_diag = maior_colun2 = mat[0][0]

for i in range(5):
    for j in range(5):
        if i == j and mat[i][j] > maior_diag:
            maior_diag = mat[i][j]
        if mat[i][j] > media:
            maior_media += 1
            maiores.append(mat[i][j])

for i in range(5):
    if mat[i][1] > maior_colun2:
        maior_colun2 = mat[i][1]

#Prints
print('   --++Matriz++--')
print('-' * 21)
for i in range(5):
    print('|', end='')
    for j in range(5):
        if mat[i][j] == maior_diag and mostra is False and i == j:
            print(f'*{mat[i][j]:2}|', end='')
            mostra = True
        elif mat[i][j] == maior_colun2 and mostra2 is False and j == 1:
            print(f'${mat[i][j]:2}|', end='')
            mostra2 = True
        else:
            print(f'{mat[i][j]:3}|', end='')
    print()

print(f'\n·Maior número da diagonal principal da matriz: *{maior_diag}')
print(f'·Maior número da coluna 2 (índice 1): ${maior_colun2}')
print(f'·Média: {media:.0f}')
print(f'·Encontrei {maior_media} números da matriz maiores que a média: {maiores}')
