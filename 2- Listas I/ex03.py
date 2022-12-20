from random import randint
idade = []
media = qtd = qtd_menor = 0

for i in range(10):
    idade.append(randint(1,120))
print(idade)

media = sum(idade) / len(idade)

for i in range(10):
    if idade[i] > 50:
        qtd += 1

    if idade[i] < media:
        qtd_menor += 1

print('A média das idades: ', media)
print('Qtde de pessoas com mais de 50 anos: ', qtd)
print('Qtde de pessoas com idade menor que a media: ', qtd_menor)
