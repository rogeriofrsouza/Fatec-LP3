"""
2.A prefeitura de uma cidade fez uma pesquisa com 10 habitantes, coletando dados sobre o salário e número de filhos.

◦Faça uma função que receba como parâmetro uma lista com os salários e retorne a média de salário da população.
◦Faça uma função que receba como parâmetro uma lista com o número de filhos e retorne a média do número de filhos.
◦Obs: Exiba no programa principal os resultados.
"""
from random import randint


def calc_salarios():
    global media_sal
    for a in range(10):
        media_sal += salarios[a]
    media_sal = media_sal / len(salarios)


def calc_filhos():
    global media_filhos
    for b in range(10):
        media_filhos += filhos[b]
    media_filhos = media_filhos / len(filhos)


# Main
salarios = []
filhos = []
media_sal = media_filhos = 0

for i in range(10):
    salarios.append(randint(1200, 4000))
    filhos.append(randint(0, 4))

calc_salarios()
calc_filhos()

# Prints
print('\n', ' ' * 8, 'PREFEITURA DE SOROCABA', ' ' * 8)
print('=' * 38)

for i in range(12):
    for j in range(3):
        if i == 0:
            if j == 0:
                print('| HABITANTES ', end='')
            elif j == 1:
                print(f'|  SALÁRIO  ', end='')
            else:
                print(f'| Nº FILHOS |')
        elif i == 1 and j == 0:
            print('=' * 38)
        elif i > 1:
            if j == 0:
                print(f'|{i-1:2}.', ' ' * 8, end='')
            elif j == 1:
                print(f'| R${salarios[i-2]:.2f} ', end='')
            else:
                if filhos[i-2] > 1:
                    print(f'| {filhos[i-2]:2} filhos |')
                elif filhos[i-2] == 1:
                    print(f'|  {filhos[i-2]:} filho  |')
                else:
                    print(f'|  -------- |')
print('=' * 38)

print(f'\n- Média de salário da população: R${media_sal:.2f}')
print(f'- Média do número de filhos: {media_filhos:.1f}')
