"""
dictonary
"""

# d1 = {'key1': 'key1 value'}
# d1['ke2'] = 'key2 value'

# print(d1['key1'])

# d1 = dict(key1='key value1', key2='key value2')
# print(d1)

# d1 = {
# 	'str': 'string',
# 	123: 'numbers',
# 	(1, 2, 3, 4, 5): 'tuple',
# }

# d1['found'] = 'haha'
# d1.update({'new_key':'new_value'})
# del d1[(1, 2, 3, 4, 5)]

# if d1.get('found') is not None:
# 	print(d1['found'])

# print(123)

# print('str' in d1)
# print('str' in d1.keys())
# print('string' in d1.values())

# d1 = {
# 	'key1': 'value 1',
# 	'key2': 'value 2',
# 	'key3': 'value 3',
# }

# for k, v in d1.items():
# 	print(k, v)

# customers = {
# 	'customer1': {
# 		'first_name': 'misa',
# 		'last_name': 'amane'
# 	},
# 	'customer2': {
# 		'first_name': 'yuuki',
# 		'last_name': 'asuna'
# 	}
# }

# for customers_k, customers_v in customers.items():
# 	print(f'showing off {customers_k}')
# 	for data_k, data_v in customers_v.items():
# 		print(f'\t{data_k} = {data_v}')

# import copy

# d1 = {1: 'a', 2: 'b', 3: 'c', 'd': ['misa', 'yui']}
# v = copy.deepcopy(d1)

# v[1] = 'lmao'
# v['d'][0] = 'waifus'

# print(d1)
# print(v) 

# l = [
# 	['c1', 1],
# 	['c2', 2],
# 	['c3', 3],
# ]


# d1 = dict(l)
# print(l)
# print(d1)

d1 = {
	1: 2,
	2: 3,
	3: 4,
	4: 5
}

d2 = {
	'a': 'b',
	'b': 'c',
	'c': 'd',
}

d1.update(d2)
print(d1)
print(d2)

# d1.pop(4)
# d1.popitem()