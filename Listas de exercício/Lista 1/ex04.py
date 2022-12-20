from random import randint
primos = mult3 = pares = media = 0
num = []
pares = []

for i in range(10):
    num.append(randint(0, 100))
    
    cont = 0
    for j in range(1, num[i]+1):
        if num[i] % j == 0:
            cont += 1
    if cont == 2:    
        primos += 1

for i in range(10):
    if num[i] % 3 == 0:
        mult3 += num[i]

    if num[i] % 2 == 0 and num[i] > 20:
        pares.append(num[i])

if len(pares) > 0:    
    media = sum(pares) / len(pares)

print(f'{num}\n')
print('RESULTADO: ')
print(f'a) Quantidade de números primos: {primos}')
print(f'b) A soma dos números múltiplos de três: {mult3}')
print(f'c) Média dos dos pares que são maiores que vinte: {media:.1f}')
    