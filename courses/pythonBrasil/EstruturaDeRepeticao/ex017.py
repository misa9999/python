# Faça um programa que calcule o fatorial de um número inteiro fornecido pelo 
# usuário. Ex.: 5!=5.4.3.2.1=120

# def fatorial(num):
#     if num == 0 or num == 1:
#         return 1
#     else:
#         return num * fatorial(num - 1)

# res = fatorial(x)
# print(f'O fatorial de {x} é {res}')

num = int(input('Digite um número para calcular o seu fatorial: '))
res = 1
for x in range(num , 0, -1):
    res *= x

print(f'O fatorial de {num} é {res}')