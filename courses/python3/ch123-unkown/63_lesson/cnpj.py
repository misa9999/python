import re


def char_remove(CNPJ):
    return re.sub(r'[^0-9]', '', CNPJ)


def validate(CNPJ):
    new_cnpj = CNPJ[:-2]
    d1 = first_digit(new_cnpj)
    d2 = second_digit(new_cnpj)
    nc = new_cnpj + d1 + d2

    if nc == CNPJ:
        return f'Valid'
    return f'Invalid'


def first_digit(CNPJ):
    reverse = 5
    total = 0

    for index in range(len(CNPJ)):
        if reverse < 2:
            reverse = 9

        total += int(CNPJ[index]) * reverse

        f_digit = 11 - (total % 11)
        reverse -= 1

    return str(f_digit)


def second_digit(CNPJ):
    reverse = 6
    total = 0
    t_cnpj = CNPJ + first_digit(CNPJ)

    for index in range(len(t_cnpj)):
        if reverse < 2:
            reverse = 9

        total += int(t_cnpj[index]) * reverse

        s_digit = 11 - (total % 11)
        reverse -= 1
        if s_digit > 9:
            s_digit = 0

    return str(s_digit)


CNPJ = input('[+] Type a CNPJ: ')
clean_cnpj = char_remove(CNPJ)

print(validate(clean_cnpj))
