from random import randint
A = []
B = []
C = []

#Preenchimento vetores
for i in range(10):
    A.append(randint(0, 50))
    B.append(randint(0, 50))

#Análise
for i in range(10):
    for j in range(10):
        if A[i] == B[j]:
            if A[i] in C:
                break
            else:
                C.append(A[i])
#Prints
print(f'Lista A: {A}')
print(f'Lista B: {B}')

C.sort()
if len(C) > 0:
    print(f'\nLista com os números que se repetem em A e B: {C}')
else:
    print('\nNenhum número se repete em A e B.')
