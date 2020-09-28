# Faça um programa que peça para n pessoas a sua idade, ao final o programa 
# devera verificar se a média de idade da turma varia entre 0 e 25,26 e 60 e 
# maior que 60; e então, dizer se a turma é jovem, adulta ou idosa, conforme 
# a média calculada

num = int(input('Número de pessoas: '))
soma = 0
for x in range(num):
    idade = int(input('Informe a idade: '))

    soma += idade

media = soma / x

calc = ''

if media <= 25:
    calc = 'jovem'
elif media <= 60:
    calc = 'adulta'
elif media > 60:
    calc = 'idosa'

print(f'Com base na média de idade a turma é {calc}')