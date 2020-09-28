# pede três números e informa o maior e o menor dele

# pede os números
n1 = int(input('N1: '))
n2 = int(input('N2: '))
n3 = int(input('N3: '))

maior = menor = n1

# verifica o maior número
if n2 > n1 and n2 > n3:
    maior = n2
elif n3 > n1 and n3 > n2:
    maior = n3
else:
    print('Os números são iguais.')

# verifica o menor número
if n2 < n1 and n2 < n3:
    menor = n2
elif n3 < n1 and n3 < n2:
    menor = n3
else:
    print('Os números são iguais')

print(f'O maior número é {maior}, e o menor número é {menor}')
