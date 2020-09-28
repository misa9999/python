# calcula o peso ideal para homens e mulheres baseado na altura
altura = float(input("Informe sua altura: "))

peso_h = (72.7 * altura) - 58
peso_m = (62.1 * altura) - 44.7

print(f'Altura {altura}')
print(f'Peso ideal homens: {peso_h:.1f}')
print(f'Peso ideal mulheres: {peso_m:.1f}')
