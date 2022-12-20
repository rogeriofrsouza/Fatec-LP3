from random import randint
L1 = []
L2 = []
res = []

#Preenchimento vetores
for i in range(10):
    L1.append(randint(0, 10))
    L2.append(randint(0, 10))

#Análises
for i in range(10):
    res.append(L1[i] * L2[i])

#Prints
print(f'Lista L1: {L1}')
print(f'Lista L2: {L2}')

print(f'\nLista resultado do produto de L1 e L2: {res}')
