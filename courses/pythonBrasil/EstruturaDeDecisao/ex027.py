'''                 Até 5 Kg           Acima de 5 Kg
Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg'''

'''Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar
R$ 25,00, receberá ainda um desconto de 10% sobre este total. Escreva um algoritmo
para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas
e escreva o valor a ser pago pelo cliente.'''


morango = int(input('Deseja comprar quantos KG de morango ? '))
maça = int(input('Deseja comprar quantos KG de maçã? '))

preçoMorango = preçoMaça = 0

if morango <= 5:
    preçoMorango = morango * 2.50
elif morango > 5:
    preçoMorango = morango * 2.20

if maça <= 5:
    preçoMaça = maça * 1.80
elif maça > 5:
    preçoMaça = maça * 1.50

preçoTotal = preçoMaça + preçoMorango

desconto = preçoTotal - (preçoTotal * 10 / 100)

print(f'total {preçoTotal:.2f}')

if morango + maça > 8 or preçoTotal > 25:
    preçoTotal = desconto

print(f"Morango --> R${preçoMorango:.2f} -- Maça --> R${preçoMaça:.2f}")
print(f'Preço total: R${preçoTotal:.2f}')
