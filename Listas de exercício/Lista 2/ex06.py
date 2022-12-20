from random import randint
A = []
B = []
C = []

#Preenchimento vetores
for i in range(10):
    A.append(randint(0, 10))
    B.append(randint(0, 10))

#Análises
for i in range(10):
    for j in range(10):
        if A[i] != B[j]:
            if A[i] in C or A[i] in B:
                break
            else:
                C.append(A[i])
for i in range(10):
    for j in range(10):
        if B[i] != A[j]:
            if B[i] in C or B[i] in A:
                break
            else:
                C.append(B[i])
#Prints
print(f'Lista A: {A}')
print(f'Lista B: {B}')

if len(C) > 0:
    print(f'\nLista com os números não repetidos entre A e B: {C}')
else:
    print('\nTodos os números são repetidos entre A e B.')
