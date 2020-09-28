# pede o preço de três produtos e informa o mais barato para comprar

# pede o preço dos produtos
p1 = float(input('produto1: R$'))
p2 = float(input('produto2: R$'))
p3 = float(input('produto3: R$'))

mais_barato = p1

# verifica o menor preço
if p2 < p1 and p2 < p3:
    mais_barato = p2
elif p3 < p1 and p3 < p2:
    mais_barato = p3

print(f'O produto mais barato custa R${mais_barato:.2f}')
