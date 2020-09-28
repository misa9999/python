# O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que 
# leia as um conjunto indeterminado de temperaturas, e informe ao final a menor e a maior 
# temperaturas informadas, bem como a média das temperaturas

maior = menor = soma = 0
num = int(input('Informe o número de temperaturas: '))
for x in range(num):
    temp = float(input('Informe a temperatura: '))
    soma += temp
    if x == 0:
        maior = menor = temp
    else:
        if temp > maior:
            maior = temp
        if temp < menor:
            menor = temp
media = soma / num 
print(f'Maior temperatura {maior} graus \-/ Menor temperatura {menor} graus, media {media} graus')