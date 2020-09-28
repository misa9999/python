# pede três números e informa o maior deles

# pede os números
n1 = int(input('n1: '))
n2 = int(input('n2: '))
n3 = int(input('n3: '))

maior = n1
# verifica o maior número
if n2 > n1 and n2 > n3:
    maior = n2
elif n3 > n1 and n3 > n2:
    maior = n3
else:
    print('Todos números são iguais')

print(f'{maior} é o maior número.')
