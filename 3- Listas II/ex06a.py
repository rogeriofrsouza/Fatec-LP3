from random import randint
A = []
B = []
C = []

for i in range(5):
    A.append(randint(0, 10))
    B.append(randint(0, 10))

for i in range(5):
    if B[i] in A:
        C.append(B[i])

print(f'A- {A}')
print(f'B- {B}')

if len(C) > 1:
    print(f'\nEncontrei {len(C)} elementos da lista B iguais a lista A:')
    print(f'C- {C}')
elif len(C) == 1:
    print(f'\nEncontrei {len(C)} elemento da lista B igual a lista A:')
    print(f'C- {C}')
else:
    print('\nNão encontrei elementos iguais nas duas listas :(')
