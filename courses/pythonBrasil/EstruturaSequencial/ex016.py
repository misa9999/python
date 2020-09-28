'''Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em
metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de
 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18
 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta
 a serem compradas e o preço total.'''

from math import ceil

area = float(input('Digite o tamanho em m²: '))

latas = ceil(area / 54)
preço_lata = 80.00

print(f'''Para cobrir uma area de {area}m² serão necessarias {int(latas)} latas
 de tintas, Total a pagar R${int(latas) * preço_lata}''')
