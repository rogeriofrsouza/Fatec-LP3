from random import randint
num = []
pares = total = media = maior_media = maior15 = qtd = pos = 0

for i in range(10):
    num.append(randint(0, 100))
    total += num[i]

media = total / len(num)
menor = num[0]

for i in range(10):
    if num[i] < menor:
        menor = num[i]
        pos = i

    if num[i] % 2 == 0:
        pares += 1

    if num[i] % 2 != 0 and num[i] > 15:
        maior15 += num[i]
        qtd += 1

    if num[i] > media:
        maior_media += 1

porcent = pares * 100 / len(num)
if qtd > 0:
    media_impares15 = maior15 / qtd

print(f'{num}\n')

print(f'Menor número da lista: {menor}, encontrado na posição: {pos}')
print(f'Porcentagem de números pares: {porcent:.1f}%')
print(f'Média dos números ímpares e maiores que quinze: {media_impares15:.1f}')
print(f'Média: {media:.1f}')
print(f'Qtd de números maiores que a média: {maior_media}')