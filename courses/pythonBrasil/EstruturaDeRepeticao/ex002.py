# le um nome de usuario e senha, se a senha for igual user printa error

while True:
    user = input('User: ')
    password = input('Password: ')

    if password != user:
        break
    else:
        print('Error password and user is the same')
