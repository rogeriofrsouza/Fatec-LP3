from random import randint
salario = []
filho = []
media_sal = media_filho = sal_menor1k = porcent = 0
c = 1

print('PREFEITURA')
print('Pesquisa de habitantes')
print('========================\n')

for i in range(10):
    print(f'{c}.')
    salario.append(float(input('- Salário: R$')))
    if salario[i] < 1000:
        sal_menor1k += 1

    filho.append(randint(0, 5))
    print(f'- Número de filhos: {filho[i]}')
    c += 1
    print('\n')

media_sal = sum(salario) / len(salario)
media_filho = sum(filho) / len(filho)
porcent = (sal_menor1k / len(salario)) * 100

print('\n' * 3)
print('Resultado Final')
print('===================')
print(f'Média de salário da população: R${media_sal:.2f}')
print(f'Média do nº de filhos: {media_filho:.2f}')
print('Maior salário: R$', max(salario))
print(f'{porcent}% da população ganha um salário inferior a R$1000')
