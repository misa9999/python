from pdb import set_trace
area = float(input('Informe o tamanho em m²: '))

set_trace()
litros = (area / 6) * 1.1  # 10% de folga
print(litros)
latas = int(litros / 18.0)
print(litros)
print(latas)
galões = int(litros / 3.6)

if litros % 18 != 0:
    latas += 1
    print(latas)
    print(litros)

if litros % 3.6 != 0:
    galões += 1

mix_latas = int(litros / 18.0)
mix_galões = int((litros - (mix_latas * 18.0)) / 3.6)
if ((litros - (mix_latas * 18.0) % 3.6 != 0)):
    mix_galões += 1


print(f'''Para cobrir uma area de {area}m²:
{latas} lata(s) -  total a pagar R${latas * 80:.2f}
{galões} galão(ões) - total a pagar R${galões * 25:.2f}
{mix_latas} latas e {mix_galões} galões - total a pagar R${(mix_latas * 80) + (mix_galões * 25)}
''')

'''comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o preço seja o menor. Acrescente 10% de
folga e sempre arredonde os valores para cima, isto é, considere latas cheias.'''
