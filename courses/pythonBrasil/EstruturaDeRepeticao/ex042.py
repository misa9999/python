"""
Faça um programa que leia uma quantidade indeterminada de números positivos e conte 
quantos deles estão nos seguintes intervalos: [0-25], [26-50], [51-75] e [76-100]. A 
entrada de dados deverá terminar quando for lido um número negativo
"""
tot1 = tot2 = tot3 = tot4 = 0
while True:
    num = int(input('Digite um número positivo, negativo para parar: '))

    if num >= 0 and num <= 25:
        tot1 += 1
    elif num >= 26 and num <= 50:
        tot2 += 1
    elif num >= 51 and num <= 75:
        tot3 += 1
    elif num >= 76 and num <= 100:
        tot4 += 1
    if num < 0:
        break
    
print()
print(f'''Números positivos no intervalor de:
[0-25] = {tot1}
[26-50] = {tot2}
[51-75] = {tot3}
[76-100] = {tot4}''')