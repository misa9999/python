def make_bold(fn):
	def wrapped():
		return f'<b>{fn()}</b>'
	return wrapped


def make_italic(fn):
	def wrapped():
		return f'<i>{fn()}</i>'
	return wrapped


def make_underline(fn):
	def wrapped():
		return f'<u>{fn()}</u>'
	return wrapped


@make_bold
@make_italic
@make_underline
def hello():
	return 'Hello World'


print(hello())