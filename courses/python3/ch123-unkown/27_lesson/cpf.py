"""
CPF = 168.995.350-09
---------------------------------------
1 * 10 = 10          #  1 * 11 = 11
6 * 9  = 54          #  6 * 10 = 60
8 * 8  = 64          #  8 * 9  = 72
9 * 7  = 63          #  9 * 8  = 72
9 * 6  = 54          #  9 * 7  = 63
5 * 5  = 25          #  5 * 6  = 30
3 * 4  = 12          #  3 * 5  = 15
5 * 3  = 15          #  5 * 4  = 20
0 * 2  = 0           #  0 * 3  = 0
                     #->0 * 2  = 0
         297         #           343
11 - (297 % 11) = 11 #  11 - (342 % 11) = 9
11 > 9 = 0           # digit 2 = 9
digit 1 = 0
"""
from random import randint
number = str(randint(100000000, 999999999))
# cpf = '16899535009'
# new_cpf = cpf[:-2]
new_cpf = number
reverse = 10
total = 0

for index in range(19):
    if index > 8:
        index -= 9

    total += int(new_cpf[index]) * reverse

    reverse -= 1
    if reverse < 2:
        reverse = 11
        d = 11 - (total % 11)

        if d > 9:
            d = 0
        total = 0
        new_cpf += str(d)

print(new_cpf)
# sequence = new_cpf == str(new_cpf[0]) * len(cpf)
# if cpf == new_cpf and not sequence:
#     print('Valid')
# else:
#     print('Invalid')

# print('CPF e.g. 168.995.350-09 ')
# cpf = input('Type a CPF: ')

# temp_cpf = ''

# for x in cpf:
#     if not x == '.' and not x == '-':
#         temp_cpf += x

# temp_cpf2 = temp_cpf
# digit_1 = ''
# digit_2 = ''
# count = 10
# total = 0

# for num in temp_cpf[:-2]:
#     total += int(num) * count
#     count -= 1


# if 11 - (total % 11) > 9:
#     digit_1 = 0
# else:
#     digit_1 = 11 - (total % 11)


# temp_cpf = temp_cpf[:-2] + str(digit_1)
# count = 11
# total = 0

# for num in temp_cpf:
#     total += int(num) * count
#     count -= 1

# if 11 - (total % 11) > 9:
#     digit_2 = 0
# else:
#     digit_2 = 11 - (total % 11)


# new_cpf = temp_cpf + str(digit_2)

# if temp_cpf2 == new_cpf:
#     print('\n\n')
#     print('Valid CPF')
# else:
#     print('Invalid CPF')
