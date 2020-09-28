"""
Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes
 de trânsito. Foram obtidos os seguintes dados:

a - Código da cidade;
b - Número de veículos de passeio (em 1999);
c - Número de acidentes de trânsito com vítimas (em 1999). Deseja-se saber:
d - Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
e - Qual a média de veículos nas cinco cidades juntas;
f - Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio
"""

x = 1
estatística = {}
cidades = []
maior = menor = mc = mn = media = soma = mediaAcidentes = somaAcidentes = total = 0
while x <= 5:
    cod = int(input('Digite o codigo da cidade: '))
    numVeiculos = int(input('Digite o número de veiculos de passeio 1999: '))
    soma += numVeiculos
    numAcidentes = int(input('Número de acidentes de transito em 1999 com vitimas: '))
    if numVeiculos <= 2000:
        somaAcidentes += numAcidentes
        total += 1
    print()
    estatística['Codigo'] = cod
    estatística['Numero de veiculos'] = numVeiculos
    estatística['Numero de acidentes'] = numAcidentes
    
    if x == 1:
        maior = menor = numAcidentes
        mc = mn = cod
    else:
        if numAcidentes > maior:
            maior = numAcidentes
            mc = cod
        if numAcidentes < menor:
            menor = numAcidentes
            mn = cod

    cidades.append(estatística.copy())
    estatística.clear()
    # print(cidade)
    
    x += 1

media = soma / 5
mediaAcidentes = somaAcidentes / total
for x in cidades:
    print(x)

print()
print(f'Maior indice de acidentes de transito: {maior}, cod cidade: {mc}')
print(f'Menor indice de acidentes de transito: {menor}, cod cidade: {mn}')
print()
print(f'A media de veiculos de todas cidades é de: {media:.0f} veiculos')
print(f'A media de acidentes nas cidades com menos de 2000 veiculos: {mediaAcidentes:.0f} veiculos')