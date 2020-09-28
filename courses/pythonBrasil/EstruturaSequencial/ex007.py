# calcula a area de um quadrado, em seguida mostra o dobro da area
def area(a, l):
    print(f'A area do quadrado é {a * l}')
    print(f'O dobro da area é {(a * l) * 2}')


a = float(input('Altura: '))
l = float(input('Largura: '))
area(a, l)
