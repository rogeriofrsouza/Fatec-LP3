"""7) A prefeitura de uma cidade fez uma pesquisa entre seus habitantes, coletando dados sobre o salário, idade e o número de filhos. Escreva um programa que leia esses dados, por exemplo para 10 pessoas. Armazene esses dados em uma matriz, depois calcule e mostre:
a) A média de salário da população
b) A média do número de filhos
c) A quantidade de filhos das pessoas que tem idade entre 15 a 25 anos
d) A média de salário de pessoas que tem idade entre 20 a 30 anos"""

from random import randint

#Variáveis
mat = []
medias_sal = medias_filhos = qtd_15a25 = tot_filhos_15a25 = media_filhos_15a25 = media_sal_20e30 = 0
cont1 = cont2 = cont3 = 0

#Preenchimento matriz
for i in range(10):
    lin = []
    lin.append(randint(1100, 5000))
    lin.append(randint(15, 70))
    lin.append(randint(0, 4))
    mat.append(lin)

#Cálculos
for i in range(10):
    medias_sal += mat[i][0]
    cont1 += 1
    medias_filhos += mat[i][2]
    cont2 += 1

    if 15 < mat[i][1] < 25:
        tot_filhos_15a25 += mat[i][2]
        qtd_15a25 += 1
    if 20 < mat[i][1] < 30:
        media_sal_20e30 += mat[i][0]
        cont3 += 1

if cont1 != 0:
    medias_sal = medias_sal / cont1
if cont2 != 0:
    medias_filhos = medias_filhos / cont2
if cont3 != 0:
    media_sal_20e30 = media_sal_20e30 / cont3
if qtd_15a25 != 0:
    media_filhos_15a25 = tot_filhos_15a25 / qtd_15a25

#Prints
print('\n' * 5)
print(' ' * 16, '..::PREFEITURA DE TANGAMANDÁPIO::..', ' ' * 15)
print('=' * 64)

for i in range(11):
    for j in range(4):
        #Tabela
        if i == 0:
            if j == 0:
                print('|', ' ' * 17, end='')
            elif j == 1:
                print('|   SALÁRIO   ', end='')
            elif j == 2:
                print(f'|    IDADE   ', end='')
            elif j == 3:
                print('|  Nº DE FILHOS  |')

        elif i <= 10:
            if j == 0:
                print(f'|  {i:2}. MORADOR(A)  |', end='')
        #Valores listas
            elif j == 1:
                print(f'  R${mat[i-1][j-1]:7.2f}  |', end='')
            elif j == 2:
                print(f'  {mat[i-1][j-1]:3} anos  |', end='')
            elif j == 3:
                if mat[i-1][j-1] > 1:
                    print(f'    {mat[i-1][j-1]} filhos    |')
                elif mat[i-1][j-1] == 1:
                    print(f'    {mat[i-1][j-1]} filho     |')
                else:
                    print(f'    --------    |')
print('=' * 64, '\n')

print(f'a) Média de salário da população: R${medias_sal:.2f}')
print(f'b) Média do número de filhos: {medias_filhos:.1f}')

if qtd_15a25 > 1:
    print(f'c) Os {qtd_15a25} habitantes com idade entre 15 e 25 anos têm: {tot_filhos_15a25} filho(s)')
elif qtd_15a25 == 1:
    print(f'c) O único habitante com idade entre 15 e 25 anos tem: {tot_filhos_15a25} filho(s)')
else:
    print(f'c) Não encontrei habitantes com idade entre 15 e 25 anos.')

print(f'    *Gerando uma média de: {media_filhos_15a25:.1f} filho(s) por habitante*')
print(f'd) Média de salário da(s) {cont3} pessoa(s) com idade entre 20 e 30 anos: R${media_sal_20e30:.2f}\n')
