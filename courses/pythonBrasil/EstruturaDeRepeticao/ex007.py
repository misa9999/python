p = 0
while p < 5:
    num = int(input(f'Num {p}: '))
    if p == 0:
        maior = num
    else:
        if num > maior:
            maior = num
    p += 1

print(f'O maior número é {maior}')