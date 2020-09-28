"""
O Sr. Manoel Joaquim acaba de adquirir uma panificadora e pretende implantar a metodologia 
da tabelinha, que já é um sucesso na sua loja de 1,99. Você foi contratado para desenvolver 
o programa que monta a tabela de preços de pães, de 1 até 50 pães, a partir do preço do pão 
informado pelo usuário, conforme o exemplo abaixo:
"""

num_paes = int(input("Informe o número de itens: "))
valor = float(input('Informe o valor do pãozinho: '))
tot = 0

if num_paes > 50:
    print('LIMITE DE 50 PRODUTOS.')
else:
    print('Lojas quase Dois - Tabela de preços')
    for x in range(num_paes):
        tot += valor
        print(f'{x+1} - R${tot:.2f}')
