nomes = []
idades = []
alturas = []
velhas = []
baixas = []
c = 1
tot_15e20 = maior_media = menor_idade = cont = menor = porcent_baixas = 0
nome_menor = ''

for i in range(5):
    print(f'\n{c}. ')
    nomes.append(input('- NOME: '))
    idades.append(int(input('- IDADE: ')))
    alturas.append(float(input('- ALTURA (m): ')))
    c += 1

media_idades = sum(idades) / len(idades)
media_alturas = sum(alturas) / len(alturas)
menor_idade = idades[0]

for i in range(5):
    if idades[i] < menor_idade:
        menor_idade = idades[i]
        nome_menor = nomes[i]

    if idades[i] >= 10 and idades[i] <= 15:
        tot_15e20 += alturas[i]
        cont += 1

    if idades[i] > media_idades:
        maior_media += 1
        velhas.append(nomes[i])

    if alturas[i] < 1.5:
        menor += 1
        baixas.append(nomes[i])

media_15e20 = tot_15e20 / cont
porcent_baixas = len(baixas) * 100 / len(alturas)

print('\n' * 10)
print('Resultado FINAL')
print('=================')

print(f'a) Menor idade: {menor_idade} anos  |  Nome: {nome_menor}')
print(f'b) Média das idades: {media_idades:.1f} anos  |  Média das alturas: {media_alturas:.2f} m')
print(f'c) Média de altura das pessoas com idade entre 10 e 15 anos (inclusive): {media_15e20:.2f} m')
print(f'd) Encontrei {maior_media} pessoa(s) com idade maior que a média: {velhas}')
print(f'e) {porcent_baixas:.0f}% das pessoas possuem altura inferior a 1.5 m: {baixas}')
