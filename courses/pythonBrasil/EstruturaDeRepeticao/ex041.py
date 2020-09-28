"""
Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes 
dados: valor da dívida, valor dos juros, quantidade de parcelas e valor da parcela.

Quantidade de Parcelas  % de Juros sobre o valor inicial da dívida
1       0
3       10
6       15
9       20
12      25

Valor da Dívida Valor dos Juros Quantidade de Parcelas  Valor da Parcela
R$ 1.000,00     0               1                       R$  1.000,00
R$ 1.100,00     100             3                       R$    366,00
R$ 1.150,00     150             6                       R$    191,67
"""
juro = val = s = parcela = 0
tot = 1

valor = float(input('Informe o valor da divida R$'))
print('Valor da Dívida - Valor dos Juros - Quantidade de Parcelas - Valor da Parcela')

l = [0, 10, 15, 20, 25]
for x in l:
    juro = valor + (valor*x/100)
    val = (valor + (valor*x/100)) - valor
    parcela = juro / tot
   
    print(f'R$ {juro:<13.2f}{val:>10.0f} {tot:>22} {parcela:>20.2f}')
    if x == 0:
        tot = 0
    tot += 3 
    










