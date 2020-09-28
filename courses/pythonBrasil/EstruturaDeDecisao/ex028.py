'''                   Até 5 Kg           Acima de 5 Kg
File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg'''

'''Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de
carne da promoção, porém não há limites para a quantidade de carne por cliente. Se
compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre
o total da compra. Escreva um programa que peça o tipo e a quantidade de carne comprada
pelo usuário e gere um cupom fiscal, contendo as informações da compra: tipo e quantidade
de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.'''


cliente = input('''O que deseja comprar?
File Duplo...R$4,90kg
Alcatra......R$5,90kg
Picanha......R$6,90kg
> ''').lower()

tipo = qtd = 0
fileDuplo = 4.90
alcatra = 5.90
picanha = 6.90

quantidade = int(input(f'Quantos KG deseja levar? '))

if quantidade > 5:
    fileDuplo = 6.80
    alcatra = 6.80
    picanha = 7.80

if cliente in 'file duplo':
    tipo = fileDuplo
    esc = "file duplo"
elif cliente in 'alcatra':
    tipo = alcatra
    esc = 'alcatra'
elif cliente in 'picanha':
    tipo = picanha
    esc = 'picanha'
else:
    print('error')

total = quantidade * tipo

pag = input('Deseja pagar com cartões Tabajara? (S/N) ')
pagam = ''
desconto = 0
if pag in 'sS':
    desconto = total - (total - (total * 5 / 100))
    pagam = 'Cartoes Tabajara'
elif pag in 'nN':
    pagam = 'A vista'

print()
print(f'''Cupom fiscal
tipo -> {esc}
quantidade -> {quantidade}kg
preço total -> R${total:.2f}
tipo de pagamento -> {pagam}
valor de desconto -> R${desconto:.2f}
valor a pagar -> R${total - desconto:.2f}''')
