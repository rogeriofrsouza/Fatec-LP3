from random import randint
pares = soma_imp = qtd_10e20 = media = 0

lista = []
for i in range(10):
    lista.append(randint(0, 100))

for i in range(10):
    if lista[i] % 2 == 0:
        pares += 1
    else:
        soma_imp += lista[i]

    if lista[i] >= 10 and lista[i] <= 20:
        qtd_10e20 += 1

media = sum(lista) / len(lista)

print(lista, '\n')
print(f'Quantidade de números pares: {pares}')
print(f'Soma dos números ímpares: {soma_imp}')
print(f'Quantidade de números entre 10 e 20: {qtd_10e20}')
print(f'Média dos números da lista: {media:.1f}')
