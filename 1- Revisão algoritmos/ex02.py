from random import randint

idade = int(randint(0, 100))

print("--------------------")
print(f"  IDADE: {idade}\n")
print("  FAIXA ETÁRIA: ", end="")

if idade >= 0 and idade <= 12:
    print("Criança...")
elif idade > 12 and idade <=17:
    print("Adolescente...")
elif idade > 17 and idade <= 59:
    print("Adulto...")
else:
    print("Idoso...")