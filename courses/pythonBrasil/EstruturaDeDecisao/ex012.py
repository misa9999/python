'''Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos
 são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3%
 para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado
 (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos.
  O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
Desconto do IR:
Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações,
 dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade
 de hora é 220.'''

# pede para que o usuário informe quanto ganha por hora
trab_hora = float(input('Quanto ganha por hora? R$'))

# pede para que o usuário informe quantas horas trabalha por mês
horas_trab = int(input('Quantas horas trabalha por mês? '))

salario_bruto = trab_hora * horas_trab

ir = 0
pct = 0
if salario_bruto <= 900:
    ir += 0
elif 900 < salario_bruto < 1500:
    ir += salario_bruto - (salario_bruto - (salario_bruto * 5 / 100))
    pct = 5
elif 1500 < salario_bruto < 2500:
    ir += salario_bruto - (salario_bruto - (salario_bruto * 10 / 100))
    pct = 10
else:
    ir += salario_bruto - (salario_bruto - (salario_bruto * 20 / 100))
    pct = 20

inss = salario_bruto - (salario_bruto - (salario_bruto * 10 / 100))
fgts = salario_bruto - (salario_bruto - (salario_bruto * 11 / 100))
tot_desc = ir + inss
salario_liquido = salario_bruto - tot_desc

print('\n')
print('-'*40)
print(f'''
Salário bruto:           R${salario_bruto:.2f}
(-) IR ({pct}%):         R${ir:.2f}
(-) INSS (10%):          R${inss:.2f}
FGTS (11%):              R${fgts:.2f}
Total de descontos:      R${tot_desc:.2f}
Salário liquido:         R${salario_liquido:.2f}
''')
print('-'*40)
print('\n')
