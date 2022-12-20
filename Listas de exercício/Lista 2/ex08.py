from random import randint
nomes = []
vendas = []
comissao = []
melhores = []
c = 1
qtd = nome_maior = 0


def titulo():
    print('._*+Registro de Vendedores+*_.')
    print('=' * 30)


titulo()
#Preenchimento vetores
for i in range(5):
    print(f'{c}.')
    nomes.append(input('Nome: '))
    vendas.append(randint(800, 2000))
    comissao.append(vendas[i] * 0.10)
    c += 1
    print()

#Cálculos
tot = sum(vendas)
media = tot / len(vendas)
maior = vendas[0]
for i in range(5):
    if vendas[i] > media:
        melhores.append(nomes[i])
        qtd += 1
    if vendas[i] > maior:
        maior = vendas[i]
        nome_maior = nomes[i]

#Prints
print('\n' * 10)
titulo()
for i in range(5):
    if vendas[i] == maior:
        print(f'-*Nome: {nomes[i]:12}  | *Vendas: R${vendas[i]:7.2f}  | *Comissão: R${comissao[i]:6.2f}   <<Maior comissão>>')
    else:
        print(f'- Nome: {nomes[i]:12}  |  Vendas: R${vendas[i]:7.2f}  |  Comissão: R${comissao[i]:6.2f}')

print(f'\nb) Total (bruto) vendido pelos 5 vendedores: R${tot:.2f}')
print(f'c) Média do total de vendas: R${media:.2f}')
print(f'd) Encontrei {qtd} vendedores acima da média: {melhores}')
