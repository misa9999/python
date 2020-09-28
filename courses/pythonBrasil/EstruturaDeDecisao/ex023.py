# pede um numero e informa se ele é inteiro ou decimal


num = input('Digite um número: ')

if '.' in num:
    num = float(num)
else:
    num = int(num)

if isinstance(num, int):
    print(f'O número {num} é inteiro')
elif isinstance(num, float):
    print(f'O numero {num} é decimal')
