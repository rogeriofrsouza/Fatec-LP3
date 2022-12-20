from random import randint
lis_A = []
lis_B = []
lis_C = []
perfeitos = []
perf = num = 0

#Preenchimento vetor
for i in range(5):
    lis_A.append(randint(1, 30))
    lis_B.append(randint(1, 30))
#Lista C = A + B
lis_C.extend(lis_A)
lis_C.extend(lis_B)

#Análises
for num in lis_C:
    cont = 0
    for i in range(1, num):
        if num % i == 0:
            cont += i
    if cont == num:
        if num in perfeitos:
            break
        else:
            perfeitos.append(num)
            perf += 1

#Prints
print(f'Lista A: {lis_A}')
print(f'Lista B: {lis_B}')
print(f'Lista C: {lis_C}\n')

if perf == 0:
    print(f'Não encontrei números perfeitos :(')
else:
    perfeitos.sort()
    print(f'Encontrei {perf} número(s) perfeito(s): {perfeitos}')
    