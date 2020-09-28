# pede dois números e mostra o maior deles
n1 = int(input('n1: '))
n2 = int(input('n2: '))

# verifica o maior número
if n1 > n2:
    print(f'Maior: n1 -> {n1}')
elif n1 < n2:
    print(f'Maior: n2 -> {n2}')
else:
    print(f'n1 e n2 -> {n1} {n2} são iguais')
