# recebe o salário de um colaborador e faz um reajuste salarial

# salários até R$ 280,00 (incluindo) : aumento de 20%
# salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
# salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
# salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
# o salário antes do reajuste;
# o percentual de aumento aplicado;
# o valor do aumento;
# o novo salário, após o aumento

salario = float(input('Digite seu salario: R$'))

# reajuste
reajuste = 0
pct = 0

# faz o reajuste conforme o salario
if salario <= 280:
    reajuste = salario + (salario * 20 / 100)
    pct = 20
elif 280 < salario < 700:
    reajuste = salario + (salario * 15 / 100)
    pct = 15
elif 700 < salario < 1500:
    reajuste = salario + (salario * 10 / 100)
    pct = 10
elif salario > 1500:
    reajuste = salario + (salario * 5 / 100)
    pct = 5

print('\n')
print(f'Salario antes do reajuste R${salario:.2f}')
print(f'O percentual de aumento foi de {pct}%')
print(f'O valor de aumento foi de R${reajuste - salario:.2f}')
print(f'O novo salário, após aumento é de R${reajuste:.2f}\n')
