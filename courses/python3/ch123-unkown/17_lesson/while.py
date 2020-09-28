
while True:
    try:
        n1 = int(input('Type a number: '))
        n2 = int(input('Type a number: '))
        print()
    except Exception as e:
        print('Type a valid number, please')
        print(f'error: {e}')
        print()
        continue

    operator = input('Type a operator: ')
    print()

    if operator == '+':
        print(f'{n1} + {n2} = {n1+n2}\n')
    elif operator == '-':
        print(f'{n1} - {n2} = {n1-n2}\n')
    elif operator == '*':
        print(f'{n1} * {n2} = {n1*n2}\n')
    elif operator == '/':
        print(f'{n1} / {n2} = {n1/n2}\n')
    else:
        print('Error, try again\n')

# while count <= 100:
#     if count == 10:
#         count += 1
#         break

#     print(count)
#     count += 1

# print('ended')

# continue
# for num in range(2, 10):
#     if num % 2 == 0:
#         print(f'Found an even number {num}')
#         continue
#     print(f'Found an odd number {num}')
# x = 2
# y = 2

# for i in range(1, 10):
#     for j in range(1, 2):
#         x += y
#     y = x

# print(x)
