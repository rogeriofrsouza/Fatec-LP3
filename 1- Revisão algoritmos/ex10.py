soma1 = soma2 = 0

print('Verificador de NÚMERO PRIMO')
print('-----------------------------')

for i in range(1, 6):
    num = int(input(f'\nDigite o {i}º número: '))
    cont = 0

    for j in range(1, num+1):
        if num % j == 0:
            cont += 1
    if cont == 2:
        print(f'{num} é PRIMO :)')
        soma1 += num
    else:
        print(f'{num} não é PRIMO :(')
        soma2 += num

print(f'\nSoma de todos os números primos: {soma1}')
print(f'Soma dos números não primos: {soma2}')
