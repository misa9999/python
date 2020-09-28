vetor = [[],[]]
stop = 0

while stop < 20:
    num = int(input('Digite um número: '))
    vetor.append(num)
    stop += 1

for x in vetor:
    if isinstance(x, float) or isinstance(x, int):
        if x % 2 == 0:
            vetor[0].append(x)
        else:
            vetor[1].append(x)

print(f'VETOR: {vetor}')
print(f'PAR: {vetor[0]}')
print(f'IMPAR: {vetor[1]}')

