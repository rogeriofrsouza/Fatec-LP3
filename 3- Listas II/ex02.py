from random import randint
A = []
B = []
C = []

for i in range(10):
    A.append(randint(2, 100))

for i in range(10):
    B.append(A[i] * min(A))

C = [0] * 20

for i in range(10):
    C[i] = A[i]

k = 10
for i in range(10):
    C[k] = B[i]
    k += 1

#C.append(A)
#C.append(B)

print('Listas')
print(f'A = {A}')
print(f'B = {B}')
print(f'C = {C}')
