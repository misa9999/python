vetor = []
consoantes = []
stop = tot = 0
while stop < 10:
    caracteres = str(input('Digite um caractere: '))
    if caracteres not in 'AEIOUaeiou':
        tot += 1
        consoantes.append(caracteres)
    vetor.append(caracteres)
    stop += 1


print(f'Vetor caracters: {vetor}')
print(f'Consoantes: {tot}')
print(f'Total de consoantes: {consoantes}')
