from random import randint


def generate_cpf():
    number = str(randint(100000000, 999999999))

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
    return f"{new_cpf[:3]}.{new_cpf[3:6]}.{new_cpf[6:9]}-{new_cpf[-2:]}"
