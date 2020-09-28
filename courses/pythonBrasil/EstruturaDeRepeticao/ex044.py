"""
Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio 
de código. Os códigos utilizados são:
1 , 2, 3, 4  - Votos para os respectivos candidatos 
(você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
5 - Voto Nulo
6 - Voto em Branco
Faça um programa que calcule e mostre:
O total de votos para cada candidato;
O total de votos nulos;
O total de votos em branco;
A percentagem de votos nulos sobre o total de votos;
A percentagem de votos em branco sobre o total de votos. Para finalizar o conjunto de 
votos tem-se o valor zero.
"""
tot1 = tot2 = tot3 = tot4 = nulo = branco = total = totB = 0
print('''
ELEIÇÃO

[1] - Ze pequeno
[2] - Cana brava
[3] - Ze maria
[4] - Borracheiro
[5] - Voto nulo
[6] - Voto em branco
''')

while True:
    voto = int(input('Deseja votar em qual candidato? '))
    
    if voto == 0:
        break
    elif voto == 1:
        tot1 += 1 
        total += 1
    elif voto == 2:
        tot2 += 1
        total += 1
    elif voto == 3:
        tot3 += 1
        total += 1
    elif voto == 4:
        tot4 += 1
        total += 1
    elif voto == 5:
        nulo += 1
        total += 1
    elif voto == 6:
        branco += 1
        total += 1
    else:
        print('Numero invalido')
        break


print(f'''
TOTAL DE VOTOS

[1] - Ze pequeno = {tot1}
[2] - Cana brava = {tot2}
[3] - Ze maria =  {tot3}
[4] - Borracheiro = {tot4}
[5] - Voto nulo = {nulo}
[6] - Voto em branco = {branco}
Percentagem de votos nulos = {(nulo/total) * 100:.0f}%
Percentagem de votos branco = {(branco/total) * 100:.0f}%
TOTAL = {total}
''')

