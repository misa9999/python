# iteration
phrase = (
    'How much wood would a woodchuck chuck if a woodchuck could chuck wood'
)

phrase_len = len(phrase)
count = 0
new_string = ''

user = input('Letter: ')

while count < phrase_len:

    letter = phrase[count]
    if letter == user:
        new_string += user.upper()
    else:
        new_string += letter
    count += 1

print(new_string)
