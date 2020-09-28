# O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e agora possui 
# uma loja de conveniências. Faça um programa que implemente uma caixa registradora rudimentar. 
# O programa deverá receber um número desconhecido de valores referentes aos preços das mercadorias.
# Um valor zero deve ser informado pelo operador para indicar o final da compra. O programa deve 
# então mostrar o total da compra e perguntar o valor em dinheiro que o cliente forneceu, para então 
# calcular e mostrar o valor do troco. Após esta operação, o programa deverá voltar ao ponto inicial,
# para registrar a próxima compra.

n = 1
tot = 0

def limpa():
    print('\n'*30)

while True:
    while True:
        preço = float(input(f'Preço {n} produto:  R$'))
        n += 1
        tot += preço
        if preço == 0:
            break 

    dinheiro = float(input('Informe a quantia em dinheiro R$'))
    print(f'Total R${tot:.2f}, troco R${dinheiro - tot:.2f}')

    opc = int(input('Digite 0 para encerrar ou 1 para continuar: (0/1)'))
    if opc == 0:
        limpa()
        print('Obrigado por comprar na nossa loja.')
        break
    elif opc == 1:
        limpa()
        n = 1
        continue
    else:
        print('Opção inválida')