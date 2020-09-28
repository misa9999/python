# pede 3 notas parciais de um aluno e mostra a media


n1 = float(input('Nota1: '))
n2 = float(input('Nota2: '))
n3 = float(input('Nota3: '))

media = (n1 + n2 + n3) / 3
sit = ""

if media == 10:
    sit = "Aprovado com distinção"
elif media >= 7:
    sit = "Aprovado"
elif media < 7:
    sit = "Reprovado"

print(f'Situação do aluno {sit} com media {media:.2f}')
