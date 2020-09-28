# Faça um programa que peça um número inteiro e determine se ele é ou não um
# número primo. Um número primo é aquele que é divisível somente por ele mesmo e por 1.

n = 0
num = int(input('Digite um número: '))
for x in range(1, num+1):
    if num % x == 0:
        n += 1

if n == 2:
    print(f'O número {num} é primo')
else:
    print(f'O número {num} não é primo')

# x = 0
# num = int(input('Digite um número: '))
# for c in range(1, num+1):
#     if num % c == 0:
#         print('\033[33m', end=' ')
#         x += 1
#     else:
#         print('\033[31m', end=' ')
#     print('{}'.format(c), end=' ')
# print('\n\033[mO número {} foi divisivel {} vezes'.format(num, x))
# if x == 2:
#     print('Portanto o número é primo')
# else:
#     print('Portando o número não é primo')