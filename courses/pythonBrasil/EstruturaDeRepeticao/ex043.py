"""
O cardápio de uma lanchonete é o seguinte:

Especificação   Código  Preço
Cachorro Quente 100     R$ 1,20
Bauru Simples   101     R$ 1,30
Bauru com ovo   102     R$ 1,50
Hambúrguer      103     R$ 1,20
Cheeseburguer   104     R$ 1,30
Refrigerante    105     R$ 1,00

Faça um programa que leia o código dos itens pedidos e as quantidades desejadas. Calcule
 e mostre o valor a ser pago por item (preço * quantidade) e o total geral do pedido.
  Considere que o cliente deve informar quando o pedido deve ser encerrado.
"""
print('''
         -- CARDÁPIO --
Especificação   Código  Preço
Cachorro Quente 100     R$ 1,20
Bauru Simples   101     R$ 1,30
Bauru com ovo   102     R$ 1,50
Hambúrguer      103     R$ 1,20
Cheeseburguer   104     R$ 1,30
Refrigerante    105     R$ 1,00
\n''')
preço = soma = 0
card = [100, 101, 102, 103, 104, 105]
p = [1.20, 1.30, 1.50, 1.20, 1.30, 1.00]
while True:
    cod = int(input('Informe o codigo do pedido: '))
    qtd = int(input('Informe a quantidade: '))
    print()

    if cod == 100:
        preço = 1.20
    elif cod == 101:
        preço = 1.30
    elif cod == 102:
        preço = 1.50
    elif cod == 103:
        preço = 1.20
    elif cod == 104:
        preço = 1.30
    elif cod == 105:
        preço = 1.00

    preço *=  qtd
    soma += preço


    # for x in card:
    #     if cod == x:
    #         print(f'Voce escolheu {cod}')


    op = str(input('Deseja continuar o pedido? ')).strip()[0]

    if op in 'nN':
        break
print(f'total R${soma:.2f}')