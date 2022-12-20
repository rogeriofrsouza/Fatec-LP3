soma = 0
print('---------------------------------')
print(' Verificador de NÚMERO PERFEITO')
print('---------------------------------\n')

for a in range(5):
    num = int(input('Digite um número: '))

    for c in range(1, num):
        if num % c == 0:
            soma+= c

    if soma == num:
        print(f'\n{num} é perfeito :)')
    else:
        print(f'\n{num} não é perfeito :(')
