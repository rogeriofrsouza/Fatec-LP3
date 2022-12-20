nomes = []
valores = []
baratos = []
caros = []
media = abaixo_10 = acima_media = maior = 0

#Preenchimento vetor
c = 1
for i in range(5):
    print(f'\n{c}º PRODUTO')
    nomes.append(input('Nome: '))
    valores.append(float(input('Preço: R$')))
    media += valores[i]
    c += 1

#Cálculos
maior = valores[0]
media = sum(valores) / len(valores)
for i in range(5):
    if valores[i] < 10:
        abaixo_10 += 1
        baratos.append(nomes[i])
    if valores[i] > media:
        acima_media += 1
        caros.append(nomes[i])
    if valores[i] > maior:
        maior = valores[i]
        nome_maior = nomes[i]

#Prints
print('\n..::Lista de compras::..')
print('=' * 27)
print('  PRODUTO       |  PREÇO')
print('-' * 27)

for i in range(5):
    if valores[i] == maior:
        print(f'-*{nomes[i]:12}  | *R${valores[i]:5.2f}*   <<Maior preço>>')
    else:
        print(f'- {nomes[i]:12}  |  R${valores[i]:5.2f}')

print(f'\na) Encontrei {abaixo_10} produto(s) com valor abaixo de R$10: {baratos}')
print(f'b) Média dos valores dos produtos: R${media:.2f}')
print(f'c) Encontrei {acima_media} produto(s) com valor acima da média: {caros}')
