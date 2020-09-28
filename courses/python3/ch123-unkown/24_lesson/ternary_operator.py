"""
ternary operator
"""

logged_user = False

msg = 'User logged in' if logged_user else 'User needs to login'

age = input('Type your age: ')

if not age.isnumeric():
    print('Please just type an integer number: ')
else:
    age = int(age)
    limit = "can access" if age >= 18 else "Can't access"

print()
print(limit)

# if logged_user:
#     msg = 'logged in'
# else:
#     msg = 'User needs to login'
