from random import randint
media = entre_20e30 = maior_media = 0
idades = []

#Preenchimento vetor
for i in range(10):
    idades.append(randint(1, 90))

menor = maior = idades[0]
media = sum(idades) / len(idades)

#Iteração vetor
for i in range(10):
    if idades[i] < menor:
        menor = idades[i]
    if idades[i] > maior:
        maior = idades[i]
    if 20 < idades[i] < 30:
        entre_20e30 += 1
    if idades[i] > media:
        maior_media += 1

#Prints
print(f'Idades: {idades}\n')
print(f'a) Menor idade: {menor} anos  |  Maior idade: {maior} anos')
print(f'b) Média das idades: {media:.0f}')
print(f'c) Pessoas com idade entre 20 e 30 anos (inclusive): {entre_20e30}')
print(f'd) Pessoas com idade maior que a média: {maior_media}')
