""" DONE
def func1(func):  # challenge 1
	return func()

def func2():
	return x + 	y

num = func1(func2)
"""

# def master(*func):
# 	return func()


# def data(**kwargs):
# 	first_name = kwargs.get('first_name')
# 	last_name = kwargs.get('last_name')
# 	age = kwargs.get('age')

# 	return first_name, last_name, age

# def my_sum(*args):
# 	total = 0
# 	for x in args:
# 		total += x
	
# 	return total

# func1, func2 = master(data(first_name='misa', last_name='amane', age=25),
# 	my_sum(1, 2, 3, 4, 5))

# print(*func1)
# print(func2)

def master(func, *args, **kwargs):
	return func(*args, **kwargs)


def names(name):
	return f'Yahallo {name}'


def greetings(name, greeting):
	return f'{greeting}, {name}'


execute = master(names, 'misa')
execute2 = master(greetings, 'misa', greeting='Good Morning')
print(execute)
print(execute2)