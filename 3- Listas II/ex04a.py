from random import randint
A = []
B = []
C = [0] * 20

for i in range(10):
    A.append(randint(0, 100))
    B.append(randint(0, 100))

k = 0
for i in range(10):
    C[k] = A[i]
    k += 1
    C[k] = B[i]
    k += 1

print(f'A - {A}')
print(f'B - {B}')
print(f'C - {C}')
