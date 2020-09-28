# pede três números e mostra em orde decrescente

# pede os números
n1 = int(input('n1: '))
n2 = int(input('n2: '))
n3 = int(input('n3: '))

maior = menor = meio = n1

# verfica o maior  número
if n2 > n1 and n2 > n3:  # n2 maior
    maior = n2
elif n3 > n1 and n3 > n2:  # n3 maior
    maior = n3

# verfica o menor número
if n2 < n1 and n2 < n3:  # n2 menor
    menor = n2
elif n3 < n1 and n3 < n2:  # n3 menor
    menor = n3

# verifica o número do meio
if n2 < maior and n2 > menor:
    meio = n2
elif n3 < maior and n3 > menor:
    meio = n3


print(maior, meio, menor)
