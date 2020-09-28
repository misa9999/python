"""
count - itertools
"""
from itertools import count


my_count = count()
names = ['misa', 'yui', 'asuna']

names = list(zip(my_count, names))

print(names)




# my_count = count(start=5, step=0.1)
# my_count = count(start=9, step=-1)


# for value in my_count:
# 	print(round(value, 2))

# 	if value >= 10 or value <= -10:
# 		break

# print(next(my_count))
# print(next(my_count))


# from types import GeneratorType
# variable = ((x, y) for x, y in zip('hello', 'hello'))

# print(isinstance(variable, GeneratorType))