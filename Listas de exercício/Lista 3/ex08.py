"""8) Escreva um programa que preencha uma lista com os nomes de 10 alunos, e outra lista com a média dos alunos. Calcule e mostre:
a) a média da classe;
b) a quantidade de alunos que tiveram média igual ou superior a 7;
c) a quantidade de alunos que tiveram média abaixo de 7;
d) a maior média da classe e nome do aluno que obteve a maior média"""

from random import randint
 
#Variáveis
nomes = []
medias = []
maior7 = []
menor7 = []
tot_media = qtd_maior7 = qtd_menor7 = maior_media = nome_maior = 0
mostraMaior = True

#Preenchimento listas
for i in range(10):
    print(f'{i+1}. Aluno(a)')
    nomes.append(input('NOME: '))

for i in range(10):
    medias.append(randint(20, 100) / 10) 
    tot_media += medias[i]
tot_media = tot_media / 10

#Cálculos
maior_media = medias[0]
for i in range(10):
    if medias[i] >= 7:
        qtd_maior7 += 1
        maior7.append(nomes[i])
    if medias[i] < 7:
        qtd_menor7 += 1
        menor7.append(nomes[i])
    if medias[i] >= maior_media:
        maior_media = medias[i]
        nome_maior = nomes[i]

#Prints
print('\n' * 5)
print(' ' * 11, '-+ESCOLA JAVALI CANSADO+-', '' * 10)
print('=' * 46)

for i in range(11):
    for j in range(3):
        #Tabela
        if i == 0:
            if j == 0:
                print('|', ' ' * 15, end='')
            elif j == 1:
                print('|', ' ' * 4, 'NOMES', ' ' * 4, end='')
            else:
                print(f'|   MÉDIA  |')

        else:
            if j == 0:
                print(f'|  {i:2}. ALUNO(A)  |', end='')
        #Valores listas
            elif j == 1:
                print(f'  {nomes[i-1]:12}  |', end='')
            else:
                if medias[i-1] == maior_media and mostraMaior == True:
                    print(f'  *{medias[i-1]:4.1f} * |   -+MAIOR MÉDIA+-')
                    mostraMaior = False
                else:
                    print(f'   {medias[i-1]:4.1f}   |')
            
print('=' * 46, '\n')

print(f'a) Média da classe: {tot_media:.1f}')
print(f'b) Encontrei {qtd_maior7} alunos com média igual ou superior a 7: \n{maior7}\n')
print(f'c) Os outros {qtd_menor7} alunos tiveram média abaixo de 7: \n{menor7}\n')
print(f'd) Maior média da classe: {maior_media}  |  Nome do aluno: {nome_maior}\n')
