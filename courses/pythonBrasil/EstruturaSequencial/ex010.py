# pede uma temperatura em celsius em seguida converte para farenheit.
graus = float(input('Informe a temperatura em °C: '))

convert = graus / 5 * 9 + 32

print(f'A temperatura de {graus:.2f}°C é correspondente a {convert:.2f}°F')
