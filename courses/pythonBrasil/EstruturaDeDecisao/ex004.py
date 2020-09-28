# verifica se uma letra é uma vogal ou consoante

# digita uma letra
letra = input('Digite uma letra: ')

# verifica se é uma vogal ou uma consoante
if letra in 'aeiouAEIOU':
    print(f'A letra -> "{letra}" é uma vogal')
else:
    print(f'A letra -> "{letra}" é uma consoante')
