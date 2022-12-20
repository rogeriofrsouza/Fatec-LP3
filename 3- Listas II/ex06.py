from random import randint

A = []
B = []
C = []
cont = index = 0

for i in range(5):
    A.append(randint(0, 10))
    B.append(randint(0, 10))

for i in range(5):
    for j in range(5):
        if B[i] == A[j] and B[i] != index:
            C.append(B[i])
            index = C[cont]
            cont += 1

print(f'A- {A}')
print(f'B- {B}')

if cont > 1:
    print(f'\nEncontrei {cont} elementos da lista B iguais a lista A:')
    print(f'C- {C}')
elif cont == 1:
    print(f'\nEncontrei {cont} elemento da lista B igual a lista A:')
    print(f'C- {C}')
else:
    print('\nNão encontrei elementos iguais nas duas listas :(')
