time = input('What time is it? ')

try:
    if float(time) < 0 or float(time) > 23:
        print('just 0-23')
    else:
        if float(time) <= 11:
            print('Good morning!')
        elif float(time) <= 17:
            print('Good evening!')
        else:
            print('Good night!')
except Exception as e:
    print('error:', e)
