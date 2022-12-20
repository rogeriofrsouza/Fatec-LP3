from random import randint
nomes = []
tel = []
c = 1

for i in range(10):
    print(f'{c}.')
    nomes.append(str(input('Nome: ')))
    tel.append(randint(981000000, 999999999))
    c += 1

print(nomes)
print(tel)
print('\n' * 3)
pesq = str(input('Digite um nome para ser pesquisado: '))
print('* Para terminar, digite: FIM\n')

while (pesq.upper() != 'FIM'):
    achou = 0
    for i in range(10):
        if nomes[i] == pesq:
            pos = i
            achou = 1
            break #vai quebrar o laço antes de terminá-lo

    if achou == 1:
        print(f'Nome: {nomes[pos]:15} - Tel: {tel[pos]}')
    else:
        print(f'{pesq} não foi encontrado :(')
    print('\n')
    pesq = str(input('Digite um nome para ser pesquisado: '))

print('T E R M I N A N D O...')