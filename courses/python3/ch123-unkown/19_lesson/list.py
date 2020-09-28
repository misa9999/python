"""
list
slicing
append, insert, pop, del, clear, extend, +
min, max
range
"""

# l1 = [1, 2, 3]
# l2 = [4, 5, 6]
# l3 = l1 + l2
# l1.extend(l2)
# l2.append('b')
# l3.insert(0, 'banana')
# l3.pop()
# del(l3[1:3])
# print(l1)
# print(l2)
# print(l3)

# l1 = list(range(1, 10))
# print(l1)

secret = 'look at the sky tonight'

typed = []

chance = 3

while True:
    if chance <= 0:
        print('YOU LOSE')
        break

    letter = input('Type a letter: ')

    if len(letter) > 1:
        print('Error, just type one letter')
        continue

    typed.append(letter)

    if letter in secret:
        print(f'Letter: "{letter}" found in secret')
    else:
        print(f'Letter: "{letter}" not found in secret')
        typed.pop()
        chance -= 1

    secret_temp = ''

    for secret_letter in secret:
        if secret_letter in typed:
            secret_temp += secret_letter
        else:
            secret_temp += '*'
    print(secret_temp)
    if secret_temp == secret:
        print(f'Found secret word: {secret_temp}')
        break

    print(f'chances {chance}')
