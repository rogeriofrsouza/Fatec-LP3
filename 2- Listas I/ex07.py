c = 1
nomes = []
massas = []
alturas = []
IMC = []
res = []

print('Calculadora de IMC')
print('=' * 15)

for i in range(5):
    print(f'{c}.')
    nomes.append(str(input('Nome: ')))
    massas.append(float(input('Massa (Kg): ')))
    alturas.append(float(input('Altura (m): ')))

    imc = massas[i] / pow(alturas[i], 2)
    IMC.append(imc)

    if IMC[i] < 18.5:
        res.append('Magreza')
    elif IMC[i] >= 18.5 and IMC[i] < 25:
        res.append('Normal')
    elif IMC[i] >= 25 and IMC[i] < 30:
        res.append('Sobrepeso')
    elif IMC[i] >= 30 and IMC[i] < 40:
        res.append('Obesidade')
    else:
        res.append('Obesidade Grave')
    c += 1

print('\n' * 10)
print('Relatório FINAL')
print('-' * 25)

for i in range(5):
    print(f'- {nomes[i]:15} | {IMC[i]:.1f} | {res[i]}')
