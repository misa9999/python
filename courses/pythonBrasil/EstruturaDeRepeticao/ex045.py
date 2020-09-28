"""
Desenvolver um programa para verificar a nota do aluno em uma prova com 10 questões, o
 programa deve perguntar ao aluno a resposta de cada questão e ao final comparar com o 
 gabarito da prova e assim calcular o total de acertos e a nota (atribuir 1 ponto por 
 resposta certa). Após cada aluno utilizar o sistema deve ser feita uma pergunta se outro
  aluno vai utilizar o sistema. Após todos os alunos terem respondido informar

a - Maior e Menor Acerto;
b -Total de Alunos que utilizaram o sistema;
c - A Média das Notas da Turma.

Gabarito da Prova:
01 - A
02 - B
03 - C
04 - D
05 - E
06 - E
07 - D
08 - C
09 - B
10 - A
"""
alunos = {}
acertos = y = maior = menor = aa = media = soma = 0
gabarito = ['A', 'B', 'C', 'D', 'E', 'E', 'D', 'C', 'B', 'A']
    
while True:
    acertos = 0
    y += 1
    p1 = str(input('Quanto é 10+2? (A=12), (B=3), (C=4), (D= 10), (E=11): '))# A
    p2 = str(input('Quanto é 10+10? (A=6), (B=20), (C=4), (D= 10), (E=11): '))# B
    p3 = str(input('Quanto é 2+2? (A=6), (B=3), (C=4), (D= 10), (E=11): '))# C
    p4 = str(input('Quanto é 3-2? (A=6), (B=3), (C=4), (D= 1), (E=11): '))# D
    p5 = str(input('Quanto é 5+5? (A=6), (B=3), (C=4), (D= 18), (E=10): '))# E
    p6 = str(input('Quanto é 30+5? (A=6), (B=3), (C=4), (D= 10), (E=35): '))# E
    p7 = str(input('Quanto é 20+20? (A=6), (B=3), (C=4), (D= 40), (E=11): '))# D
    p8 = str(input('Quanto é 7+2? (A=6), (B=3), (C=9), (D= 10), (E=11): '))# C
    p9 = str(input('Quanto é 1+1? (A=6), (B=2), (C=4), (D= 10), (E=11): '))# B
    p10 = str(input('Quanto é 9+9? (A=18), (B=3), (C=4), (D= 10), (E=11): '))# A
    print()

    if p1 in 'aA':
        acertos += 1
    if p2 in 'bB':
        acertos += 1
    if p3 in 'cC':
        acertos += 1
    if p4 in 'dD':
        acertos += 1
    if p5 in 'eE':
        acertos += 1
    if p6 in 'eE':
        acertos += 1
    if p7 in 'dD':
        acertos += 1
    if p8 in 'cC':
        acertos += 1
    if p9 in 'bB':
        acertos += 1
    if p10 in 'aA':
        acertos += 1
    soma += acertos
    alunos[y] = acertos
    op = str(input('Deseja utilizar o sistema para outro aluno? '))
    if op in 'nN':
        break

for k, v in alunos.items():
    if k == 1:
        maior = menor = v
        ma = mn = k
    else:
        if v > maior:
            maior = v
            ma = k
        if v < menor:
            menor = v
            mn = k
    print(f'"ALUNO {k}" ACERTOS = {v}')

media = soma / y
print()
print(f'Maior nota {maior} "aluno {ma}", menor nota "{menor} aluno {mn}"')
print(f'Total de alunos que usaram o sistema: {y}')
print(f'A media da turma é de {media}')