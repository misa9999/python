"""
Faça um programa que calcule o valor total investido por um colecionador em sua coleção 
de CDs e o valor médio gasto em cada um deles. O usuário deverá informar a quantidade de 
CDs e o valor para em cada um
"""


qtd_cds = int(input("Informe a quantidade de cds comprados: "))

total = t = 0
for x in range(qtd_cds):
    val = float(input("Informe o valor de cada cd R$"))
    t += 1
    print(f"Valor do {x+1} cd R${val:.2f}")
    total += val

print(f"Quantidade de {t} cds, valor total R${total:.2f}")
