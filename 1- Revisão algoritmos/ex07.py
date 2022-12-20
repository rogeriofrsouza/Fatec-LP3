import os
def clear(): os.system('cls')
maior_idade = maior_altura = tot_altura = media = 0
menor_idade = 120

for c in range (1, 6):
    clear()
    print('\n' * 80)  # prints 80 line breaks

    print('ATLETA ', c)
    print('-------------\n')
    idade = int(input('IDADE: '))
    altura = float(input('ALTURA: '))

    tot_altura += altura
    if idade > maior_idade:
        maior_idade = idade
    if idade < menor_idade:
        menor_idade = idade
    if altura > maior_altura:
        maior_altura = altura

media = float(tot_altura / c)
print('\n'*80) # prints 80 line breaks

print(f'\nMaior idade: {maior_idade}')
print(f'Menor idade: {menor_idade}')
print(f'Média das alturas: {media:.2f}')
print(f'Maior altura: {maior_altura}')
