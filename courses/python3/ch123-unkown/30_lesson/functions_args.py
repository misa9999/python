"""
functions - *args **kwargs
"""

# def func(*args):
# 	args = list(args)
# 	args[0] = 30
# 	print(args)

# func(1, 2, 3, 4, 5)

# l = [1,2,3,4,5]
# print(*l, sep=' -> ')
# n1, n2, *n = l

# names = ['misa', 'yuuki', 'yui', 'luffy', 'zoro']
# print(*names, sep='\n')

# names = 'cookies.com.br'
# names1 = names.split('.')
# print(names1)
# names2 = '.'.join(names1)
# print(names2)

def func(*args, **kwargs):
	print(args)

	first_name = kwargs.get('first_name')
	last_name = kwargs.get('last_name')
	age = kwargs.get('age')
	weight = kwargs.get('weight')

	print(first_name, last_name, age)
	if weight is not None:
		print(weight)

l1 = [1, 2, 3, 4, 5]
l2 = [10, 20, 30, 40, 50]
func(*l1, *l2, first_name='misa', last_name='amane', age=25)