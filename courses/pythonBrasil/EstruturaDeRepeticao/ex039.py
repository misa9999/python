"""
Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o 
número do aluno e o segundo representando a sua altura em centímetros. Encontre o aluno 
mais alto e o mais baixo. Mostre o número do aluno mais alto e o número do aluno mais 
baixo, junto com suas alturas.
"""

alunos = {}
x = 1
ma = mn = aa = ab = 0

while x <= 10:
    num = int(input('Digite o numero do aluno: '))
    altura = float(input('Digite a altura do aluno: '))
    print()
    
    if x == 1:
        ma = mn = altura
        aa = ab = num
    else:
        if altura > ma:
            ma = altura
            aa = num
        if altura < mn:
            mn = altura
            ab = num

    alunos[num] = altura
    x += 1

print()
for k, v in alunos.items():
    print(f'"Aluno {k}" altura = {v:.2f}')

print(f'"Aluno mais alto {aa}" = {ma:.2f}, "Aluno mais baixo {ab}" = {mn:.2f}')
