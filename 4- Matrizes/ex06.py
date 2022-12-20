from random import randint
mat = []
valores = []
media_lin3 = soma_col2 = entre_5e15 = 0

#Preenchimento matriz
for i in range(4):
    lin = []
    for j in range(3):
        lin.append(randint(0, 30))
    mat.append(lin)
    if i == 2:
        media_lin3 = sum(mat[i]) / len(mat[i])

#Iteração matriz
for i in range(4):
    soma_col2 += mat[i][1]
for lin in mat:
    for valor in lin:
        if 5 < valor < 15:
            entre_5e15 += 1
        valores.append(valor)

#Prints
print('  *_.Matriz._+')
print('=' * 16)
for i in range(4):
    print('| ', end='')
    for j in range(3):
        print(f'{mat[i][j]:3}| ', end='')
    print()

print(f'\n◦Média dos números da 3ª linha (índice 2): {media_lin3:.0f}')
print(f'◦Soma dos números da 2ª coluna (índice 1): {soma_col2}')
print(f'◦Quantidade de números entre 5 e 15 na matriz: {entre_5e15}')
print(f'◦Números da matriz: {valores}')
