# def div(n1, n2):
# 	try:
# 		return n1 / n2
# 	except ZeroDivisionError as error:
# 		print('log:', error)
# 		raise


# try:
# 	print(div(2, 0))
# except ZeroDivisionError as error:
# 	print(error)


def div(n1, n2):
	if n2 == 0:
		raise ValueError("N2 not 0")
	return n1 / n2

try:
	print(div(2, 0))
except ValueError as error:
	print(error)