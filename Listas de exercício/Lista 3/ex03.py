"""3) Escreva um programa que leia uma matriz de ordem 5 x 4, onde na 1ª coluna da matriz são armazenados os nomes dos vendedores, da 2ª coluna a 4ª coluna são armazenados o total de vendas por mês de cada vendedor, portanto na 2ª coluna é armazenado a venda do mês 1, 3ª coluna do mês 2 e na 4ª coluna do mês 3. Calcule e mostre na tela:
a) O valor total vendido por vendedor
b) A maior venda do mês 1
c) A menor venda do mês 3
d) O total vendido por mês"""

from random import randint

#Variáveis
mat = []
trimestre = []
totais = []
total = k = 0

#Preenchimento matriz
for i in range(5):
    lin = []
    for j in range(4):
        if j == 0:
            lin.append(input(f'{i+1}. Nome vendedor(a): '))
        else:
            lin.append(randint(800, 4000))
    mat.append(lin)

#Cálculos
for i in range(5):
    tot_vendedor = 0
    for j in range(1, 4):
        tot_vendedor += (mat[i][j])
    trimestre.append(tot_vendedor)

maior_mes1 = mat[0][1]
menor_mes3 = mat[0][3]
for i in range(5):
    if mat[i][1] > maior_mes1:
      maior_mes1 = mat[i][1]
    if mat[i][3] < menor_mes3:
      menor_mes3 = mat[i][3]

for a in range(1, 4):
    tot_col = 0
    for b in range(5):
        tot_col += mat[b][a]
    totais.append(tot_col)
totais.append(sum(trimestre))

#Prints
print('\n' * 5)
print(' ' * 31, '..::RELATÓRIO FINAL::..', ' ' * 31)
print('=' * 87)

for i in range(8):
    for j in range(6):
        #Tabela
        if i == 0:
            if j == 0:
                print('|', ' ' * 15, end='')
            elif j == 1:
                print('|', ' ' * 4, 'NOMES', ' ' * 4, end='')
            elif j <= 4:
                print(f'|    MÊS {j-1}   ', end='')
            elif j == 5:
                print('|  TRIMESTRE |')

        elif i <= 5:
            if j == 0:
                print(f'| {i}. VENDEDOR(A) |', end='')
        #Valores listas
            elif j == 1:
                print(f' {mat[i-1][j-1]:14} |', end='')
            elif j <= 4:
              if mat[i-1][j-1] == maior_mes1 or mat[i-1][j-1] == menor_mes3:
                print(f'*R${mat[i-1][j-1]:8.2f}*|', end='')
              else:
                print(f' R${mat[i-1][j-1]:8.2f} |', end='')
            elif j == 5:
                print(f' R${trimestre[k]:8.2f} |')
                k += 1
            
        elif i == 6:
            if j == 0:
                print('|', ' ' * 14, '|', ' ' * 15, end='')
                print('|', ' ' * 10, '|', ' ' * 10, '|', ' ' * 10, '|', ' ' * 10, '|')
        #Total colunas
        elif i > 6:
            if j == 0:
                print(f'| {i-1}. TOTAL ', ' ' * 5, end='')
            elif j == 1:
                print('|', ' ' * 14, '|', end='')
            elif j <= 4:
                print(f' R${totais[j-2]:8.2f} |', end='')
            elif j == 5:
                print(f' R${totais[j-2]:8.2f} |', end='')
            elif j == 6:
                print(f' R${totais[j-2]:8.2f} |')
print()
print('=' * 87, '\n')

print(f'- A maior venda do MÊS 1: R${maior_mes1:.2f}')
print(f'- A menor venda do MÊS 3: R${menor_mes3:.2f}\n')
