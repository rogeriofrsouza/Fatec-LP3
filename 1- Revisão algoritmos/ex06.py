import os
Pesado = Velho = Maior90 = SomaPesos = Media50 = Magros = 0
cont = 1
opcao = string = 's'

while opcao == 'S' or opcao == 's':
    os.system('cls')
    print('---------------------------')
    print(f' Maior idade: {Velho} anos')
    print(f' Maior peso: {Pesado} Kg')
    print('---------------------------\n')

    print(f'Cliente {cont}')
    idade = int(input('IDADE: '))
    if idade > Velho:
        Velho = idade

    peso = float(input('PESO (Kg): '))
    if peso > Pesado:
        Pesado = peso
    if peso > 90:
        Maior90 += 1
    if peso < 50:
        SomaPesos += peso
        Magros += 1

    cont += 1
    opcao = str(input('\nQuer continuar? [S/N] \n'))

os.system('cls')
print('-------------------------------')
print(f' Maior idade: {Velho} anos')
print(f' Maior peso: {Pesado} Kg')
print('-------------------------------\n')

Media50 = SomaPesos / Magros
print(f'Pessoas com mais de 90 Kg: {Maior90}')
print(f'Média da idade de pessoas com menos de 50 Kg: {Media50}')
