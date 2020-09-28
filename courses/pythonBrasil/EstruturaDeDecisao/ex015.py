# pede os três lados de um triângulo  e informa se pode formar um triângulo
# verifica quais o tipo de triângulo: equilátero, isósceles ou escaleno

# pede os lados dos triângulo
l1 = float(input('lado1: '))
l2 = float(input('lado2: '))
l3 = float(input('lado3: '))

tipo = ""

# verifica se pode formar um triângulo
# verifica se a soma de dois lados é maior que o terceiro lado
if l1 + l2 > l3 and l1 + l2 > l3 and l2 + l3 > l1:
    # verifica se todos lados são iguais
    if l1 == l2 == l3:
        tipo = "EQUILÁTERO"
    # verifica se dois lados são iguais
    elif l1 == l2 != l3 or l1 == l3 != l2 or l2 == l3 != l1:
        tipo = "ISÓSCELES"
    # verifica se todos lados são diferentes
    else:
        tipo = "ESCALENO"
    print(f'Pode formar um triângulo {tipo}')
else:
    print('Não pode formar um triângulo')
