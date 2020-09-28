"""
functions
"""


def greetings(msg='Yahallo', name='Misa'):
    return f'{msg} {name}'


print(
    f'{greetings()}\n'
    f'{greetings(name="Yuuki")}\n'
    f'{greetings("Hi", "Yukinoshita")}\n'
    f'{greetings(name="Yui", msg="Ohayou")}')
