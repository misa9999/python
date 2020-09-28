user = input('User: ')
number_characters = len(user)

if number_characters < 6:
    print('You must enter at least 6 characters.')
else:
    print('You have successfully registered and logged in.')

str1 = input('Type something: ')
str2 = input('Type something else: ')

print(f'The total number of characters entered was: {len(str1) + len(str2)}')
