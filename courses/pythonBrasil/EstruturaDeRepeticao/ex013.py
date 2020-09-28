# Faça um programa que peça dois números, base e expoente, calcule e mostre o 
# primeiro número elevado ao segundo número. Não utilize a função de potência 
# da linguagem.

base = int(input('Digite a base: '))
exp = int(input('Digite o expoente: '))
e = base
for x in range(1, exp):
    e *= base

print(f'{base} elevado a {exp} -> {e}')