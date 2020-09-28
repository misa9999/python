maior = menor = 0 
for x in range(5):
    num = int(input('Digite um número: '))

    if num < 0 or num > 1000:
        print('Digite apenas números entre 0 e 1000')
        break

    if x == 0:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

print(f'Maior num -> {maior} Menor -> {menor} soma deles -> {maior + menor}')