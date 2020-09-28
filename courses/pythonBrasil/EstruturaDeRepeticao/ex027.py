"""
Faça um programa que calcule o número médio de alunos por turma. Para isto, peça a
quantidade de turmas e a quantidade de alunos para cada turma. As turmas não podem ter
mais de 40 alunos
"""

qtd_turmas = int(input("Digite a quantidade de turmas: "))

soma = t = 0

for x in range(qtd_turmas):
    qtd_alunos = int(input("Digite a quantidade de alunos: "))
    soma += qtd_alunos

media = soma / t

if media > 40:
    print("As turmas não podem ter mais de 40 alunos.")
else:
    print(f"a media de alunos por turmas é de {int(media)} alunos.")
