# Altere o programa de cálculo dos números primos, informando, caso o número não seja primo, por quais número ele é divisível.

x = 0
num = int(input('Digite um número: '))
for c in range(1, num+1):
    if num % c == 0:
        print('\033[33m', end=' ')
        x += 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end=' ')
print('\n\033[mO número {} foi divisivel {} vezes'.format(num, x))
if x == 2:
    print('Portanto o número é primo')
else:
    print('Portando o número não é primo')