"""
List comprehension
"""

# l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# eg1 = [variable for variable in l1]

# eg2 = [v * 2 for v in l1]

# eg3 = [(v, v2) for v in l1 for v2 in range(3)]

# l2 = ['misa', 'yui', 'asuna']

# eg4 = [v.replace('a', '@') for v in l2]

# tuple_ = (
# 	('key1', 'value1'),
# 	('key2', 'value2'),
# )

# eg5 = [(y, x) for x, y in tuple_]	
# eg5 = dict(eg5)

# l3 = list(range(100))

# eg6 = [v for v in l3 if v % 3 == 0 if v % 8 == 0]

# even = []
# odd = []

# # eg7 = [v if v % 2 == 0 and v % 8 == 0 else 0 for v in l3]
# eg7 = [even.append(v) if v % 2 == 0 else odd.append(v) for v in l3]

# print(f'even: {even}')
# print(f'odd: {odd}')



############# NEW ################

numbers = [1, 2, 3, 4, 5]

def div(x, y):
	return x / y


def mul(x, y):
	return x * y


def po(x, y):
	return x ** y


print(numbers)