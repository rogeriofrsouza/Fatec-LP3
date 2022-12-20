cont1 = cont2 = soma = media = maior_num = tot_mult3 = media_mult3 = primos = so_mult5 = qtd = 0
num = cont = 1

print('Vamos calcular?\n')
print('REGRAS:')
print('1)Para calcular, digite um nº maior que zero')
print('2)Para terminar, digite zero ou um nº negativo')

while num > 0:
    num = int(input(f'\nDigite o {cont}º número: '))
    soma += num
    cont1 += 1
    cont += 1
    qtd = 0

    if num > maior_num:
        maior_num = num

    if num % 3 == 0 and num != 0:
        tot_mult3 += num
        cont2 += 1

    for i in range(1, num + 1):
        if num % i == 0:
            qtd += 1
    if qtd == 2:
        primos += 1

    if num % 5 == 0 and num != 0:
        so_mult5 += 1

    if cont1 == 10:
        print('\nLembrete: Para finalizar, digite zero ou um nº negativo')

cont1 -= 1
media = soma / cont1
if cont2 > 0:
    media_mult3 = tot_mult3 / cont2
else:
    media_mult3 = 0

print('\n' * 80)
print('RESULTADO FINAL')
print('----------------\n')
print(f'- Soma dos números digitados: {soma}')
print(f'- Média dos números digitados: {media:.2}')
print(f'- Maior número digitado: {maior_num}')
print(f'- Média dos números múltiplos de três: {media_mult3:2}')

if primos > 1:
    print(f'- Encontrei {primos} números primos...')
elif primos == 1:
    print(f'- Encontrei apenas {primos} número primo...')
elif primos == 0:
    print('- Não encontrei nenhum número primo :(')

if so_mult5 > 1:
    print(f'- Encontrei {so_mult5} números múltiplos de cinco...')
elif so_mult5 == 1:
    print(f'- Encontrei {so_mult5} número múltiplo de cinco...')
elif so_mult5 == 0:
    print('- Não encontrei nenhum número múltiplo de cinco :(')
