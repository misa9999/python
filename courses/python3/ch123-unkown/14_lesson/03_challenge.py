name = input('Name: ')

if len(name) <= 4:
    print('your name is too short')
elif len(name) == 5 or len(name) == 6:
    print('your name is normal')
else:
    print('your name is too big')
