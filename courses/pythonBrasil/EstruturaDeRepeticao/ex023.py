# Faça um programa que mostre todos os primos entre 1 e N sendo N um número 
# inteiro fornecido pelo usuário. O programa deverá mostrar também o número de
# divisões que ele executou para encontrar os números primos. Serão avaliados
# o funcionamento, o estilo e o número de testes (divisões) executados.

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