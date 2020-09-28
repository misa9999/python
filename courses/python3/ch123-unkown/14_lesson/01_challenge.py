num = input('Type a number: ')

try:
    if int(num) % 2 == 0:
        print(f'{num} is even')
    else:
        print(f'{num} is odd')
except Exception as e:
    print(f"'{num}' isn't integer number")
    print(f'ERROR: {e}')
