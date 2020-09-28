# Faça um programa que receba dois números inteiros e gere os números inteiros
#  que estão no intervalo compreendido por eles.

num1 = int(input('Num1: '))
num2 = int(input('Num2: '))

print(f'Os números entre {num1} e {num2} são -> ', end='')

for x in range(num1+1, num2):
    print(x, end=' ')    
    
print()
    