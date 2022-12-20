from random import randint
mat = []
media = mult_3 = par_maior10 = 0

#Preenchimento matriz
for i in range(5):
    lin = []
    for j in range(3):
        lin.append(randint(0, 50))
    mat.append(lin)
    media += sum(lin)

#Iteração matriz
for lin in mat:
    for valor in lin:
        if valor % 3 == 0:
            mult_3 += 1
        if valor % 2 == 0 and valor > 10:
            par_maior10 += valor
media = media / 15

#Prints
print(' +-._Matriz_.-+')
print('=' * 16)
for i in range(5):
    print('| ', end='')
    for j in range(3):
        print(f'{mat[i][j]:3}| ', end='')
    print()
print(f'\na)Qtd de números múltiplos de três: {mult_3}')
print(f'b)Soma dos números pares e maiores que dez: {par_maior10}')
print(f'c)Média dos números armazenados na matriz: {media:.0f}')
