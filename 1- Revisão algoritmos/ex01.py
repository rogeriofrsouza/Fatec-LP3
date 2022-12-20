from random import randint

pares = SomaPares = menor10 = 0

for i in range(10):
    # num = int(input("Digite um valor: ")
    num = int(randint(1, 20))

    if num % 2 == 0:
        pares += 1
        SomaPares = SomaPares + num
    if num < 10:
        menor10 += 1

print(f"Encontrei {pares} valores pares \n")
print(f"Soma dos números pares: {SomaPares} \n")
print(f"Números inferiores a 10: {menor10} \n")
