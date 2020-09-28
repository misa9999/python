'''Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar.
O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
par ou ímpar;
positivo ou negativo;
inteiro ou decimal'''

n1 = int(input('Num1: '))
n2 = int(input('Num2: '))

op = input('''Qual operação deseja usar:
[ + ] - soma
[ - ] - subtração
[ * ] - multiplicação
[ / ] - divisão
> ''')

result = 0

if op == '+':
    result = n1 + n2
elif op == '-':
    result = n1 - n2
elif op == '*':
    result = n1 * n2
elif op == '/':
    result = n1 / n2
else:
    print('Opção inválida')

print(f'{n1} {op} {n2} = {result}')

if result % 2 == 0:
    print(f'O número {result} é par')
else:
    print(f'O número {result} é impar')

if result < 0:
    print(f'O número {result} é negativo')
else:
    print(f'O número {result} é positivo')

if isinstance(result, int):
    print(f'O número {result} é inteiro')
elif isinstance(result, float):
    print(f'O número {result} é decimal')
