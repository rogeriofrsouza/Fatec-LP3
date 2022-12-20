from random import randint
A = []
B = []
C = []

for i in range(10):
    A.append(randint(0, 100))
    B.append(randint(0, 100))
    C.append(A[i])
    C.append(B[i])

print(f'A - {A}')
print(f'B - {B}')
print(f'C - {C}')
