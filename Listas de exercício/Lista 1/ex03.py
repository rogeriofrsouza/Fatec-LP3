cont = opcao = idade = opiniao = 1
qtd1 = qtd2 = qtd3 = tot_idade = 0

print('CINEMA FATEC')
print('==============')

while idade > 0:
    mudou = False
    print(f'\n{cont}º Espectador')

    idade = int(input('Digite sua idade: '))
    tot_idade += idade

    if idade > 0:
        while mudou == False:
            print('\nOpinião em relação ao filme?')
            opiniao = int(input('3- ótimo; 2- bom; 1- regular: '))   

            if opiniao == 3:
                qtd3 += 1
                mudou = True
            elif opiniao == 2:
                qtd2 += 1
                mudou = True
            elif opiniao == 1:
                qtd1 += 1
                mudou = True
            else:
                print('ERRO: Digite uma opção do menu...\n')

        cont += 1
        if cont == 3:
            print('\n*Para finalizar, digite uma idade negativa ou zero*')

cont -= 1
media = tot_idade / cont

print('\nRESULTADO: ')
print(f'a) Quantidade de pessoas que responderam ótimo: {qtd3}')
print(f'b) Quantidade de pessoas que responderam bom: {qtd2}')
print(f'c) Quantidade de pessoas que responderam regular: {qtd1}')  
print(f'd) Média das idades das pessoas: {media:.1f}') 
