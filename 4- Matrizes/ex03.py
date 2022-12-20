from random import randint
mat_A = []
mat_B = []
mat_C = []

for i in range(2):
    lin = []
    for j in range(2):
        lin.append(randint(1, 20))
    mat_A.append(lin)

for i in range(2):
    lin = []
    for j in range(2):
        lin.append(randint(1, 20))
    mat_B.append(lin)

print('Matriz A')
for i in range(2):
    print(mat_A[i])

print('\nMatriz B')
for i in range(2):
    print(mat_B[i])

for i in range(2):
    lin = []
    for j in range(2):
        lin.append(mat_A[i][j] + mat_B[i][j])
    mat_C.append(lin)

print('\nMatriz C')
for i in range(2):
    print(mat_C[i])
