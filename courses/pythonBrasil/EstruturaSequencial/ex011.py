# pede dois números inteiros e um número real em seguida calcula
# A - o produto do dobro do primeiro com metade do segundo .
# B - a soma do triplo do primeiro com o terceiro.
# c - o terceiro elevado ao cubo.
n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite outro número inteiro: '))
n3 = float(input('Digite um número real: '))

print(f'A -> {int((n1 * 2) + (n2 / 2))}')
print(f'B -> {(n1*3) + n3}')
print(f'C -> {n3**3}')
