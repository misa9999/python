# calcula o salário mensal com base no salário/hora, horas/mês

ganha_hora = float(input('Quanto você ganha por hora? R$'))
horas_trab = int(input('Quantas horas trabalha por mês? '))
tot_sal = ganha_hora * horas_trab

print(f'''você ganha R${ganha_hora:.2f} hora, você trabalhou {horas_trab} horas este mês, seu
salário total no fim do mês será de R${tot_sal:.2f}
''')
