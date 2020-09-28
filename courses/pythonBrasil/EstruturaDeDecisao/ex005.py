# pede duas notas de um aluno. Verifica se ele foi aprovado, repr ou apro com dt

# pede as notas
n1 = float(input('nota1: '))
n2 = float(input('nota2: '))

# soma a media
media = (n1 + n2) / 2

# verifica se o aluno foi aprovado, reprovado ou aprovado com distinção
if media == 10:
    print(f'Média: {media:.1f}, Aluno aprovado com distinção')
elif media >= 7:
    print(f'Média: {media:.1f}, Aluno APROVADO!')
else:
    print(f'Média: {media:.1f}, Aluno REPROVADO!')
