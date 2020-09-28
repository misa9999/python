# calcula o valor da multa por kilo excedido no limite de peso de 50kg

peso = 50
multa = 4.00

peixe = int(input('Informe quantos kg de peixe possui: '))
if peixe > peso:
    m = (peixe - peso) * multa
    print(f'Valor da multa R${m:.2f}')
else:
    print('Abaixo do limite.')
