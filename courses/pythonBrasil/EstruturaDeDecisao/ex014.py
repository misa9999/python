# lê duas notas parciais de um aluno ao longo de um semestre

# pede as notas
n1 = float(input('Nota1: '))
n2 = float(input('Nota2: '))
print('\n')

média = (n1 + n2) / 2
conc = ""
sit = ""

# verifica a situação atual do aluno com base na média
if 9.0 < média < 10.0:
    conc = 'A'
    sit = 'APROVADO'
elif 7.5 < média <= 9.0:
    conc = "B"
    sit = "APROVADO"
elif 6.0 < média <= 7.5:
    conc = "C"
    sit = "APROVADO"
elif 4.0 < média <= 6.0:
    conc = "D"
    sit = "REPROVADO"
else:
    conc = "E"
    sit = "REPROVADO"

print(f'''Notas do aluno x:
Nota1: {n1:.2f}
Nota2: {n2:.2f}
Média: {média:.2f}
Conceito: {conc}
Situação:  {sit}
''')
