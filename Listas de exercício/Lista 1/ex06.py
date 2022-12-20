cont = idade = 1
idades = []
qtd_20e40 = maior = menor = tot_idade = 0

while idade > 0:

    idade = int(input(f'\n{cont}. Digite sua idade: '))
    if idade > 0:
        idades.append(idade)

        if idade >= 20 and idade <= 40:
            qtd_20e40 += 1
    
        if cont == 1:
            maior = idade
            menor = idade
        else:
            if idade > maior:
                maior = idade
            elif idade < menor:
                menor = idade
    
    tot_idade += idade

    cont += 1
    if cont == 3:
        print('\n*Para finalizar, digite uma idade negativa ou zero*')

media = sum(idades) / len(idades)

print('\n' * 3)
print(f'Idades: {idades}\n')

print(f'a) Quantidade de pessoas com idade entre 20 e 40 anos: {qtd_20e40}')
print(f'b) Maior idade: {maior}')
print(f'c) Menor idade: {menor}')
print(f'd) A média das idades: {media:.1f}')
