"""
conditions: IF, ELIF, ELSE
"""


# age = int(input('Age: '))

# if age < 18:
#    print('kid')
# elif age >= 18 and age <= 30:
#    print('young')
# elif age > 30 and age <= 45:
#    print('adult')
# else:
#    print('old')

"""RELATIONAL OPERATORS

== equal
> >= greater than
< <=
!= different

"""

# name = input('Name: ')
# age = int(input('Age: '))
# max_age = 18

# if age >= 20 and age <= 30:
#    print(f'{name} can get a loan')
# else:
#    print(f"{name} can't get a loan")

"""LOGIC OPERATORS

and, or, not
in, not in
"""

# a = 2
# b = 3

# if not b > a:
#     print('b > a')
# else:
#     print('a > b')

# void = ''

# if not void:
#     print('Please write anything in void')

# print('\n\n')

# name = 'Misa'

# if 'a' in name:
#     print('found letter "a"')
# else:
#     print('not found')

user = input('User: ')
password = input('Password: ')

user_bd = 'misa'
password_bd = '123456'

if user == user_bd and password == password_bd:
    print('Login success')
    key = input('Key: ')
    if not key:
        print('Please enter key')
    else:
        print('Success!')
else:
    print('Invalid username or password')
