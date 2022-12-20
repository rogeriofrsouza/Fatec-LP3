tot_maior_50a90kg = peso_30e50 = cont_30e50 = tot_altura = tot_15e25 = cont_15e25 = 0
med_30e50 = med_total = med_15e25 = 0
for i in range(1, 6):
    print(f'Cadastro {i}')
    idade = int(input('IDADE (anos): '))
    altura = float(input('ALTURA (m): '))
    peso = int(input('PESO (Kg): '))

    if idade > 50 and peso > 90:
        tot_maior_50a90kg += 1

    if idade >= 30 and idade <=50:
        peso_30e50 += peso
        cont_30e50 += 1

    tot_altura += altura

    if idade >= 15 and idade <= 25:
        tot_15e25 += altura
        cont_15e25 += 1

    print('\n' * 10)

print('LISTAGEM FINAL')
print('----------------\n')
print(f'Pessoas com idade superior a 50 anos e que pesam mais que 90 quilos: {tot_maior_50a90kg}')

if cont_30e50 > 0:
    med_30e50 = peso_30e50 / cont_30e50
print(f'Média do peso das pessoas com idade entre 30 e 50 anos: {med_30e50:.2f}')

med_total = tot_altura / 5
print(f'Média da altura de todas pessoas: {med_total:.2f}')

if cont_15e25 > 0:
    med_15e25 = tot_15e25 / cont_15e25
print(f'Média de altura da pessoas com idade entre 15 e 25 anos: {med_15e25:.2f}')

