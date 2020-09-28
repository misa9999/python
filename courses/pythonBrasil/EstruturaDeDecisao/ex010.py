# pede para inforar o turno de estudo, em seguida da uma saudação no turno esp

# pergunta o turno de estudo M-matutino V-vespertino N-noturno
horario = input('Turno de estudo: M-matutino/V-vespertino/N-noturno: ')

if horario in 'mM':
    print('Bom dia!')
elif horario in 'vV':
    print('Boa tarde!')
elif horario in 'nN':
    print('Boa noite!')
else:
    print('Valor inválido!')
