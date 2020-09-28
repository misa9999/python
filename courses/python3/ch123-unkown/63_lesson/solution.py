
import re
import random


REGRESSIVE = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]


def validate(cnpj):
    cnpj = char_remove(cnpj)

    try:
        if is_sequence(cnpj):
            return False
    except Exception as e:
        return False

    try:
        new_cnpj = calculate_digit(cnpj=cnpj, digit=1)
        new_cnpj = calculate_digit(cnpj=new_cnpj, digit=2)
    except Exception as e:
        return False

    if new_cnpj == cnpj:
        return True
    return False


def calculate_digit(cnpj, digit):
    if digit == 1:
        reg = REGRESSIVE[1:]
        new_cnpj = cnpj[:-2]
    elif digit == 2:
        reg = REGRESSIVE
        new_cnpj = cnpj
    else:
        return None

    total = 0
    for index, regressive in enumerate(reg):
        total += int(cnpj[index]) * regressive

    digit = 11 - (total % 11)
    digit = digit if digit <= 9 else 0

    return f'{new_cnpj}{digit}'


def is_sequence(cnpj):
    sequence = cnpj[0] * len(cnpj)

    if sequence == cnpj:
        return True

    return False


def char_remove(cnpj):
    return re.sub(r'[^0-9]', '', cnpj)


def generate():
    first_digit = random.randint(0, 9)
    second_digit = random.randint(0, 9)
    second_block = random.randint(100, 999)
    third_block = random.randint(100, 999)
    fourth_block = '0001'

    start_cnpj = f'{first_digit}{second_digit}{second_block}' \
        f'{third_block}{fourth_block}00'

    new_cnpj = calculate_digit(cnpj=start_cnpj, digit=1)
    new_cnpj = calculate_digit(cnpj=new_cnpj, digit=2)

    return new_cnpj


def format_cnpj(cnpj):
    cnpj = char_remove(cnpj)
    # 04.252.011/0001-10
    # 04252011000110
    return f'{cnpj[:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}-{cnpj[-2:]}'
