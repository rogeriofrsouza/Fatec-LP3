from random import randint
medias_times = []
idades = []
massas = []
alturas = []
menor_idade = tot_idades = tot_alturas = pesado = cont = 0

for i in range(5):
    tot_idades = media_idades = 0
    for j in range(11):
        idade = randint(16, 45)
        idades.append(idade)
        massa = randint(50, 100)
        massas.append(massa)
        altura = randint(150, 200)/ 100
        alturas.append(altura)

        if idade < 18:
            menor_idade += 1

        tot_idades += idade
        tot_alturas += altura
        
        if massa > 80:
            pesado += 1

    media_idades = tot_idades / 11
    medias_times.append(media_idades)

media_alturas = tot_alturas / 55
porcent = pesado * 100 / 55

print('CAMPEONATO FATEC')
print('=================')

for i in range(0, 55, 1):
    if i == 0 or i == 11 or i == 22 or i == 33 or i == 44 or i == 55:
        print('\n')
        cont += 1
        print(f'Time {cont}')

    print(f'- Idade: {idades[i]} anos  |  Massa: {massas[i]:3} Kg  |  Altura: {alturas[i]:.2f} m')
    
print(f'\na) Quantidade de jogadores com idade inferior a 18 anos: {menor_idade}')
print('b) Média das idades dos jogadores: ')
cont = 1
for i in range(5):
    print(f'Time {cont}: {medias_times[i]:.1f} anos')
    cont += 1

print(f'c) Média das alturas de todos os jogadores do campeonato: {media_alturas:.1f} m')
print(f'd) Porcentagem de jogadores com mais de 80 quilos entre todos do campeonato: {porcent:.0f}%')
