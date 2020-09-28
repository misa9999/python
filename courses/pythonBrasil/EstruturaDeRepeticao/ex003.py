"""Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';
"""
stop = False
while True:
    while True:
        name = input('name: ')
        if len(name) >= 3:
            break

    while True:
        idade = int(input('idade: '))
        if 0 < idade < 150:
            break

    while True:
        salario = float(input('Salario: '))
        if salario > 0:
            break

    while True:    
        sexo = input('sexo: f/m ')
        if sexo in 'fmFM':
            break
    
    while True:
        estado_civil = input('estado civil: s, c, v, d ')
        if estado_civil in 'scvdSCVD':
            break
    stop = True

    if stop:
        break
    



