from random import randint
num= []
fat = []

for i in range(10):
    num.append(randint(0, 15))
    f = 1

    for j in range(2, num[i]+1):
        f = f * j

    fat.append(f)

print('Lista Final')
print('=============\n')

for i in range(10):
    print(f'- Nº digitado: {num[i]:3} | Fatorial: {fat[i]}')
