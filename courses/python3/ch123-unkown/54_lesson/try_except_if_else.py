def number_convert(value):
	# if value.isnumeric():
	# 	return float(value)
	# return str(value)
	try:
		value = int(value)
		return value
	except ValueError as error:
		try:
			value = float(value)
			return value
		except:
			pass


number = number_convert(input('[*] Enter A Number: '))
if number is None:
	print('not number')
else:
	print(number * 5)
