"""Altere o programa anterior permitindo ao usuário informar as populações e as 
taxas de crescimento iniciais. Valide a entrada e permita repetir a operação."""

pop1 = int(input('pop1: '))
taxa1 = float(input('Taxa1: '))
pop2 = int(input('pop2: '))
taxa2 = float(input('Taxa2: '))


p = 0
while True:
    x = pop1 # 3% anual
    y = pop2 # 1.5% anual

    p1 = (x + (x * taxa1 / 100)) - x
    p2 = (y + (y * taxa2 / 100)) - y

    for k in range(p):
        x += p1
        y += p2

    p3 = (x + (x * taxa1 / 100)) - x
    p4 = (y + (y * taxa2 / 100)) - y


    for k in range(p):
        x += p3
        y += p4

    p += 1

    if x >= y:
        print(f'População atual de Pais A -> {int(x)} habitantes')
        print(f'População atual de Pais B -> {int(y)} habitantes')
        print(f'Levaram {p} anos para Pais A ultrapassar Pais b')        
        break