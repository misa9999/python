# Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. 
# Ex.: 5!=5.4.3.2.1=120. A saída deve ser conforme o exemplo abaixo:


num = int(input('Digite um número para calcular o seu fatorial: '))
res = 1
print(f'{num}!=', end='')
for x in range(num , 0, -1):
    res *= x
    if x == 1:
        print(x, end='=')
    else:
        print(x, end='.')
print(res)
