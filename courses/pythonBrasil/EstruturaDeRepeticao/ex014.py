# Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade
#  de números pares e a quantidade de números impares.

p = i = c = 0
while c < 10:
    num = int(input('Num: '))

    if num % 2 == 0:
        p += 1
    else:
        i += 1
    c +=1


print(f'Números: (PARES {p}) (IMPARES {i})')
