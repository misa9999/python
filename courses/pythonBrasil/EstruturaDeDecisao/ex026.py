'''
Um posto está vendendo combustíveis com a seguinte tabela de descontos:
Álcool:
até 20 litros, desconto de 3% por litro
acima de 20 litros, desconto de 5% por litro
Gasolina:
até 20 litros, desconto de 4% por litro
acima de 20 litros, desconto de 6% por litro
Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível
(codificado da seguinte forma:
A-álcool, G-gasolina), calcule e imprima o
valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro
do álcool é R$ 1,90
'''

alcool = 1.90
gasolina = 2.50



# pede os litros a serem abastecidos
litros = int(input('Abastecer quantos litros? '))

# preço total sem descontos do alcool e da gasolina
totalAlcool = litros * alcool
totalGasolina = litros * gasolina

descontoAlcool = descontoGasolina = 0

def calcula(litros):
    if litros <= 20:
        descontoAlcool = totalAlcool - (totalAlcool * 3 / 100)
        descontoGasolina = totalGasolina - (totalGasolina * 4 / 100)
    elif litros > 20:
        descontoAlcool = totalAlcool - (totalAlcool * 5 / 100)
        descontoGasolina = totalGasolina - (totalGasolina * 6 / 100)


    print(f'''A-alcool -> R$1,90 / G-gasolina -> R$2,50
Total sem descontos -> A(R${totalAlcool:.2f}) G(R${totalGasolina:.2f})
Preço final --> A(R${descontoAlcool:.2f}) G(R${descontoGasolina:.2f})''')

    
calcula(litros)
