# 4 notas de 10 alunos, calcule e armazene num vetor a media de cada aluno, em seguida imprimir numero de alunos com media maior que 7


alunos = []
aluno = []
medias = []

stop = media = tot = 0


while stop < 10:
    aluno.clear()
    for x in range(4):
        nota = float(input(f'Digite a {x+1} nota: '))
        aluno.append(nota)

    print()
    alunos.append(aluno[::])
    stop += 1


for lista in alunos:
    total = 0
    for x in lista:
        total += x
    media = total / 4
    medias.append(media)

for x in medias:
    if x > 7:
        tot += 1

print(f'O total de alunos com media maior que 7 é de {tot} alunos')