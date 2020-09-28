# Faça um programa que, dado um conjunto de N números, determine o menor valor,
#  o maior valor e a soma dos valores.

maior = menor = 0 
for x in range(5):
    num = int(input('Digite um número: '))

    if x == 0:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

print(f'Maior num -> {maior} Menor -> {menor} soma deles -> {maior + menor}')