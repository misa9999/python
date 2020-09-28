# Numa eleição existem três candidatos. Faça um programa que peça o número 
# total de eleitores. Peça para cada eleitor votar e ao final mostrar o número 
# de votos de cada candidato.

mais_vot = patinhas = batatinha = zezinho = 0

tot_ele = int(input('Digite o número total de eleitores: '))

print('''Escolha seu canditado:
[ 1 ] patinhas
[ 2 ] batatinha
[ 3 ] zezinho''')
for x in range(tot_ele):
    voto = int(input(f'{x+1}° Eleitor: '))
    
    if voto == 1:
        patinhas += 1
    elif voto == 2:
        batatinha += 1
    elif voto == 3:
        zezinho += 1
    else:
        print('ERRO candidato invalido')

print(f'''Numero de votos
Patinhas -> {patinhas}
Batatinha -> {batatinha}
Zezinho -> {zezinho}''')