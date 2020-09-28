"""
Supondo que a população de um país A seja da ordem de 80000 habitantes com uma
taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes 
com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o 
número de anos necessários para que a população do país A ultrapasse ou iguale
a população do país B, mantidas as taxas de crescimento.
"""
p = 0
while True:

    x = 80000 # 3% anual
    y = 200000 # 1.5% anual

    p1 = (x + (x * 3 / 100)) - x
    p2 = (y + (y * 1.5 / 100)) - y

    for k in range(p):
        x += p1
        y += p2

    p3 = (x + (x * 3 / 100)) - x
    p4 = (y + (y * 1.5 / 100)) - y


    for k in range(p):
        x += p3
        y += p4

    p += 1

    if x >= y:
        print(f'População atual de Pais A -> {int(x)} habitantes')
        print(f'População atual de Pais B -> {int(y)} habitantes')
        print(f'Levaram {p} anos para Pais A ultrapassar Pais b')        
        break