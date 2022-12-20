from random import randint
maior15 = media = menor_media = j = maior = pos = 0
c = 1
nomes = []
idades = []
menores = []

for i in range(10):
    print(f'Aluno {c}:')
    nomes.append(str(input('NOME: ')))
    idades.append(randint(1, 120))
    print(f'IDADE: {idades[i]}')
    print('=================')

    c += 1
    print('\n' * 2)

media = sum(idades) / len(idades)

for i in range(1, 10):
    if idades[i] < media:
        menor_media += 1
        menores.append(nomes[i])

    if idades[i] > 15:
        maior15 += 1

    if idades[i] > maior:
        maior = idades[i]
        pos = i

print('\n' * 5)
print('LISTA DE FINAL')
print('=================')
print(f'Encontrei {maior15} alunos com idade superior a 15 anos')
print(f'A media de idade dos alunos é: {media:.2f}')
print(f'Os alunos {menores} possuem idade abaixo da média')
print(f'{nomes[pos]} tem a maior idade, que é: {maior}')


