#Faça um programa que leia 5 números e informe a soma e a média dos números.

p = soma = 0 
while p < 5:
    num = int(input(f'{p} num: '))

    soma += num 
    p += 1

media = soma / p
print(f'A soma dos números é {soma} e a média é {media}')