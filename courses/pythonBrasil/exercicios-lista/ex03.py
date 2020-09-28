notas = []
n = media =  0
while n < 4:
    nota = float(input(f'Digite a {n+1} nota: '))
    notas.append(nota)
    n += 1

soma = sum(notas)
media = soma/n
for x in notas:
    print(f'Nota: {x}')

print(f'Media: {media}')