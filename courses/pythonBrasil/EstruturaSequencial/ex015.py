# pergunta o quanto ganha por hora e quantos horas trabalhadas durante o mês
# A salário bruto.
# B quanto pagou ao INSS.
# C quanto pagou ao sindicato.
# D o salário líquido.
dinheiro_hora = float(input('Quanto ganha por hora? R$'))
horas_mes = int(input('Quantas horas trabalha por mês? '))

salário_bruto = dinheiro_hora * horas_mes
ir = salário_bruto - (salário_bruto - (salário_bruto * 11 / 100))
inss = salário_bruto - (salário_bruto - (salário_bruto * 8 / 100))
sindicato = salário_bruto - (salário_bruto - (salário_bruto * 5 / 100))
salário_liquido = salário_bruto - ir - inss - sindicato

print(f'''
+ Salário Bruto R${salário_bruto:.2f}
- IR (11%): R${ir:.2f}
- INSS (8%): R${inss:.2f}
- Sindicato (5%): R${sindicato:.2f}
= Salário Liquido: R${salário_liquido:.2f}
''')
