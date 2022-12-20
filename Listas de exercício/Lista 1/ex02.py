from random import randint
primos = media1 = media2 = 0
num = []
mult3_maior10 = []
entre10e30 = []

for i in range(10):
    num.append(randint(0, 100))
    cont = 0
    for j in range(1, num[i]+1):
        if num[i] % j == 0:
            cont += 1
    if cont == 2:    
        primos += num[i]

for i in range(10):
    if num[i] % 3 == 0 and num[i] > 10:
        mult3_maior10.append(num[i])

    if num[i] >= 10 and num[i] <= 30:
        entre10e30.append(num[i])

if len(mult3_maior10) > 0:    
    media1 = sum(mult3_maior10) / len(mult3_maior10)
if len(entre10e30) > 0:
    media2 = sum(entre10e30) / len(entre10e30)

print(f'{num}\n')
print('RESULTADO: ')
print(f'a) Soma dos números primos: {primos}')
print(f'b) Média dos nºs múltiplos de três e maiores que dez: {media1:.1f}')
print(f'c) Média dos nºs maiores ou iguais a dez e menores ou iguais a trinta: {media2:.1f}')
    