# Faça um programa que calcule o mostre a média aritmética de N notas.

p = soma = 0
while p < 5:
    nota = float(input('Digite as notas: '))

    soma += nota
    p += 1

media = soma / p
print(f'A média do aluno foi {media}')