'''Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois
 informar quantas notas de cada valor
serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo
 de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.
Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma
 nota de 1;
Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma
nota de 5 e quatro notas de 1'''


saque = float(input('Informe o valor do saque: R$'))

# total recebe o valor de saque
total = saque
# cedula de 100 reais
ced = 100
# total de cedulas
total_cedulas = 0

# loop infinito
while True:
    # verofoca se p valo total é maior que a maior cedulas
    if total >= ced:
        # caso seja maior total recebe total menos a cedula
        total -= ced
        # enqanto true add mais uma cedula ao numero de cedulas
        total_cedulas += 1
    else:
        # se o total de ced for maior que 0 printa o total e a quantidade de cedulas usadas
        if total_cedulas > 0:
            print(f'Total de cedulas {total_cedulas} cedulas de R${ced:.2f}')
        if ced == 100:
            ced = 50
        elif ced == 50:
            ced = 10
        elif ced == 10:
            ced = 5
        elif ced == 5:
            ced = 1
        total_cedulas = 0
        if total == 0:
            break
