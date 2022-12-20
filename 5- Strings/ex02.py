"""Faça um programa que peça como entrada 2 palavras, em seguida junte essas duas palavras em uma string e
depois faça uma busca de uma palavra ou sílaba nessa string usando find()."""

print('Google das Strings')
print('-' * 18)

palavra1 = input('Digite uma palavra: ')
palavra2 = input('Digite outra palavra: ')

palavra_final = palavra1 + ' ' + palavra2
print(f'\nJuntando tudo temos: {palavra_final}')

opcao = input(f'\nGostaria de realizar uma busca em {palavra_final}? [S/N] ')

while opcao.upper() != 'N':
    busca = input('Digite a sua pesquisa: ')
    pos = palavra_final.find(busca)

    if pos != -1:
        print(f'\nEncontrei {busca} em {palavra_final} :)')
    else:
        print(f'\nNão encontrei {busca} :(')

    opcao = input(f'\nGostaria de continuar? [S/N] ')

print('\nOk, terminando...\n')
