'''Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2
+ bx + c. O programa deverá pedir os valores de a, b e c e fazer as consistências,
informando ao usuário nas seguintes situações:
Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e
o programa não deve fazer pedir os demais valores, sendo encerrado;
Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário
 e encerre o programa;
Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao
 usuário;
Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;'''

from math import sqrt

a = int(input('A: ')) # 5
b = int(input('B: ')) # 3
c = int(input('C: ')) # 2

delta = (b**2) -4 * a * c

xa = -b + sqrt(delta)
x1 = xa / (2 * a)

xb = -b - sqrt(delta)
x2 = xb / (2 * a)

if a == 0:
    print('A equação não é de segundo grau')
    exit()
if delta < 0:
    print(f'A equação não possui raizes reais -> {delta}')
elif delta == 0:
    ...
elif delta > 0:
    print(f'A equação possui duas raizes reais: {x1} e {x2}')

print(delta)
print(x1)
print(x2)
