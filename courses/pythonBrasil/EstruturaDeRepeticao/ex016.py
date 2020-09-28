# A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,... 
# Faça um programa que gere a série até que o valor seja maior que 500.

n = int(input('Digite os termos: '))
t1 = 0
t2 = 1
cont = 1
print(f'{t1} → {t2} → ', end='')
while cont < n:
    t3 = t1 + t2
    if t3 > 500:
        break
    print(f'{t3} → ', end='')
    t1 = t2
    t2 = t3
    cont += 1
print('Fim.')
