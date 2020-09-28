# pede uma temperatura em farenheit em seguida converte para celsius.
graus = float(input('Informe a temperatura em °F: '))

convert = (5 * (graus-32) / 9)

print(f'A temperatura de {graus:.2f}°F é correspondente a {convert:.2f}°C')
