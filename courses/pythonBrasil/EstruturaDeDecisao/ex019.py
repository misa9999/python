# le um número inteiro menor que 1000 e imprime a quantidade de centena, dezena e unidade


# pede um número intenro menor que mil
num = int(input('Digite um número inteiro menor que 1000: '))

u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10

print(f'O número {num} possui {c} centenas, {d} dezenas e {u} unidades')
