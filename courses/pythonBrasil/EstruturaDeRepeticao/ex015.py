# A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... 
# Faça um programa capaz de gerar a série até o n−ésimo termo.

# def fibonacci(num):
#     if num <= 1:
#         return num
#     else:
#         return fibonacci(num - 1 ) + fibonacci(num - 2)

# x = int(input('Digite um número: '))
# res = fibonacci(x - 1)

# print(f'O fibonacci de {x} é {res}')


n = int(input('Digite os termos: '))
t1 = 0
t2 = 1
cont = 1
print('{} → {} → '.format(t1, t2), end='')
while cont < n:
    t3 = t1 + t2
    print('{} → '.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1
print('Fim.')
