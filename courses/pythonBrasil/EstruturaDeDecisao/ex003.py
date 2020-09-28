# verifica se uma letra digitada é F - fem ou M - mascu ou sexo inválido.

# pede uma letra
letra = input('Digite F ou M: ').strip()

# verifica se é F - fem ou M masc
if letra in 'fF':
    print('Feminino')
elif letra in 'mM':
    print('Masculino')
else:
    print('Sexo inválido.')
