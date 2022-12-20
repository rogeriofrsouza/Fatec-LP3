from random import randint
c = 1
nomes = []
idades = []
massa = []

for i in range(10):
    print(f'{c}.')
    nomes.append(input('NOME: '))
    idades.append(randint(1, 100))
    massa.append(randint(30, 120))
    c += 1
print('\n' * 3)

opcao = 'S'
while opcao.upper() != 'N':
    pesq = input('Digite um nome para pesquisar: ')
    if pesq in nomes:
        idx = nomes.index(pesq)
        print('Encontrei :)')
        print(f'{idx+1}. Nome: {nomes[idx]:15} | Idade: {idades[idx]:3} anos | Massa: {massa[idx]:3} Kg.')

    else:
        print('\nEste nome não foi encontrado :(')

    opcao = input('\nGostaria de pesquisar novamente? [S/N] ')

print('T E R M I N A N D O...')
