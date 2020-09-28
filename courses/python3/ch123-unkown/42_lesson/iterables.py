# lists tuples str -> Sequences -> Iterable

name = 'Misa Amane'
iterator = iter(name)
generator = (letter for letter in name)

print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))

for letter in generator:
	print(letter)

# try:
# 	print(next(iterator)) # M
# 	print(next(iterator)) # I
# 	print(next(iterator)) # S
# 	print(next(iterator)) # A
# 	print(next(iterator)) 
# except:
# 	pass

# print('end\n')

# for value in iterator:
# 	print(value)