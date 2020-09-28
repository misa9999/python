import json


d1 = {
	'People 1': {
		'name': 'Misa',
		'age': 25,
	},
	'People 2': {
		'name': 'Lucy',
		'age': 22,
	},
	'People 3': {
		'name': 'Asuna',
		'age': 20,
	},
}


def create_json(dict):
	return json.dumps(dict, indent=True)


# with open('people.json', 'w') as f:
# 	f.write(create_json(d1))

with open('people.json', 'r') as f:
	d1_json = f.read()
	d1_json = json.loads(d1_json)

for k, v in d1_json.items():
	print(k)
	for k1, v1 in v.items():
		print('\t', k1, v1)


# with open('abc.txt', 'a+') as file:
# 	file.write('new_line\n')
# 	file.seek(0)
# 	print(file.read())

# with open('abc.txt', 'r') as file:
# 	print(file.read())

# with open('abc.txt', 'w+') as file:
# 	file.write('line 1\n')
# 	file.write('line 2\n')
# 	file.write('line 3\n')

# 	file.seek(0)
# 	print(file.read())


# try:
# 	file = open('abc.txt', 'w+')
# 	file.write('line')
# 	file.seek(0)
# 	print(file.read())
# finally:
# 	file.close()

# file = open('abc.txt', 'w+')
# file.write('Line 1\n')
# file.write('Line 2\n')
# file.write('Line 3\n')

# file.seek(0, 0)
# print('Lines: ')
# print(file.read())
# print('############\n')

# file.seek(0, 0)
# print(file.readline().strip('\n'))
# print(file.readline().strip('\n'))
# print(file.readline().strip('\n'))

# print('############\n')
# file.seek(0, 0)
# # for line in file.readlines():
# # 	print(line.strip('\n'))

# for line in file:
# 	print(line.strip('\n'))

# file.close()