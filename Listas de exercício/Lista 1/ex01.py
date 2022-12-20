from random import randint
tot_pares = impares = maior_20 = 0
num = []
maior_20 = []

for i in range(10):
    num.append(randint(0, 100))
    if num[i] % 2 == 0 and num[i] > 10:
        tot_pares += num[i]

    if num[i] % 2 != 0:
        impares += 1

    if num[i] > 20:
        maior_20.append(num[i])

media = sum(maior_20) / len(maior_20)
menor = num[0]

for i in range(10):
    if num[i] < menor:
        menor = num[i]

print(f'{num}\n')
print('RESULTADO:')
print(f'a) O menor número: {menor}')
print(f'b) Soma dos números pares e maiores que dez: {tot_pares}')
print(f'c) Quantidade de números ímpares: {impares}')
print(f'd) a média dos números maiores que vinte: {media:.1f}')
