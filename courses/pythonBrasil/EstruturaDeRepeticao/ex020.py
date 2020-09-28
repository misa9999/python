# Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o 
# fatorial várias vezes e limitando o fatorial a números inteiros positivos e 
# menores que 16.

while True:
    num = int(input('Digite um número para calcular o seu fatorial: '))
    if num < 0 or num > 16:
        print('ERROR apenas numeros positivos e menores que 16')
        break
    res = 1
    for x in range(num , 0, -1):
        res *= x
    
    print(f'O fatorial de {num} é {res}')