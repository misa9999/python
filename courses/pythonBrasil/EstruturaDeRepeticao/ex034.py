# Os números primos possuem várias aplicações dentro da Computação, por exemplo na Criptografia.
# Um número primo é aquele que é divisível apenas por um e por ele mesmo. Faça um programa que 
# peça um número inteiro e determine se ele é ou não um número primo.

n = 0
num = int(input('Digite um número: '))
for x in range(1, num+1):
    if num % x == 0:
        n += 1

if n == 2:
    print(f'O número {num} é primo')
else:
    print(f'O número {num} não é primo')