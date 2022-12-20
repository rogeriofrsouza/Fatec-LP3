from random import randint
c = 1
lista = []
fatorial = []

for i in range(10):
    fat = 1
    lista.append(randint(1, 15))

    for j in range(2, lista[i]+1):
        fat = fat * j
    fatorial.append(fat)

print('Relatório FATORIAL')
print('====================')

for i in range(10):
    print(f'- Número: {lista[i]:2} | Fatorial: {fatorial[i]}')
    c += 1
