# pede uma nota entre 0 e 10, mostra uma mensagem de erro caso valor errado

# while infinito enqquanto o número não for entre 0 e 10
while True:
    num = int(input('Digite um número de 0 a 10: '))

    if num > 10:
        print('Error valor incorreto digite novamente')
    else:
        print(f'Você digitou {num}')
        break
