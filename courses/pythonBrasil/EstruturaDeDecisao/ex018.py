# pede uma data no formato dd/mm/aaaa e informa se é válida

# pede uma data
dia = int(input('Informe o dia: '))
mês = int(input('Informe o mês: '))
ano = int(input('Informe o ano: '))
''
if 0 < dia < 31 and 1 < mês <= 12 and 1000 < ano < 9999:
    print(f'Data {dia}/{mês}/{ano}')
else:
    print('Data inválida')  


