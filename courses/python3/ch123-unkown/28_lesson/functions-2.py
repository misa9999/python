# def function(var):
# 	return var


# variable = function('msg')

# if variable:
# 	print(variable)
# else:
# 	print('error')

# def div(n1: int, n2: int) -> int:
# 	if n1 <= 0 or n2 <= 0:
# 		return f'Error! please enter number greater than "0"'

# 	return n1 / n2

# div_nums = div(8, 2)
# print(div_nums)

def f(var):
	print(var)


def dumb():
	return f

var = dumb()
var('my value')