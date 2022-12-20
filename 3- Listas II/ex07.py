from random import randint

nomes = []
vendas = []
comissao = []
res = []
maior_media = 0
c = 1

for i in range(5):
    print(f'\n{c}.')
    nomes.append(input('NOME: '))
    vendas.append(randint(800, 2000))
    comissao.append(vendas[i] * 0.10)
    c += 1

maior_comis = comissao[0]
nome = nomes[0]

total = sum(vendas)
media = total / len(nomes)

for i in range(5):
    if vendas[i] > media:
        maior_media += 1
        res.append(nomes[i])

    if comissao[i] > maior_comis:
        maior_comis = comissao[i]
        nome = nomes[i]

print('\n' * 10)
print('Resultado do Mês')
print('==================\n')

print('a)')
for i in range(5):
    print(f'- Nome: {nomes[i]:15} | Valor a receber: R${comissao[i]:.2f}')

print(f'\nb) Total (bruto) vendido pelos 5 vendedores: R${total:.2f}')
print(f'c) Média do total de vendas: R${media:.2f}')

if maior_media >= 1:
    print(f'\nd) {maior_media} vendedor(es) acima da média das vendas:')
    for i in range(maior_media):
        print(f'- {res[i]}')
else:
    print('Nenhnum vendedor acima da média de vendas :(')

print(f'\ne) Maior valor de comissão: R${maior_comis:.2f}\n   Vendedor que recebeu: {nome}')
