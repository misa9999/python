variable = 'value' # global scope


def func():
	other_variable = 'value 2'
	return other_variable

def func2(arg):
	print(arg)


var = func()
func2(var)