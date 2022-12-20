print('FATORIAL')
print('---------\n')

for c in range(1, 4):
    num = int(input(f'Digite o {c}º valor: '))
    f = 1
    for i in range(2, num+1):
        f = f * i
        if i == num:
            print(f'{i} = {f}\n')
        else:
            print(f'{i} x ', end='')

print('Ufa... terminei ._.')
