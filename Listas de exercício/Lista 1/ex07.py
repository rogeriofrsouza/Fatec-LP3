opcao = "S"
import time

print('Cálculo de TABUADA')
print('====================')

while opcao.upper() != "N":
    num = int(input('\nEscolha um nº de 1 a 10: '))

    if num >= 1 and num <= 10:
        print('\n' * 2)
        print('CALCULANDO . . .\n')
        time.sleep(3)

        for i in range(11):
            tab = num * i
            print(f'{num:2}  x {i:2} = {tab:3}') 

        opcao = input('\nGostaria de continuar? [S/N] ')

print('\nTERMINANDO . . .')