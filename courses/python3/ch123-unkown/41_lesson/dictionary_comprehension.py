"""
DICTIONARY COMPREHENSION
"""

l1 = [
	('key 1', 'value 1'),
	('key 2', 'value 2'),
	('key 3', 'value 3'),

]

# d1 = {k.upper(): v.upper() for k, v in l1}
# d1 = {v for v in range(5)} # set comprehension
# d1 = {f'key_{v}': v**2 for v in range(5)}
d1 = {f'{v}^2 = ': v**2 for v in range(5)}
print(d1)