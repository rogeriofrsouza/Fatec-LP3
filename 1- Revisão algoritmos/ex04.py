from random import randint

somaNotas = 0
SoMenor6 = 0

for i in range(1, 11):
    nota = float(randint(0, 10))
    somaNotas += nota
    if nota < 6:
        SoMenor6 += 1

media = somaNotas / 10

print(f'Média da classe: {media}')
print(f'Encontrei {SoMenor6} alunos com nota menor de 6')
