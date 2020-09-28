from string import ascii_lowercase as alpha
from operator import mod
from functools import partial


t = len(alpha)


def calc(letter, type='encrypt'):
	# if type == 'encrypt':
	# 	return alpha[mod((alpha.index(letter) + 3), t)]
	# return alpha[mod((alpha.index(letter) - 3), t)]

	if type == 'encrypt':
		exp = alpha.index(letter) + 3
	else:
		exp = alpha.index(letter) - 3
	return alpha[mod(exp, t)]


dec = partial(calc, type='decrypt')


def encrypt(phrase: str) -> str:
	# l = []
	# for letter in phrase:
	# 	l.append(calc(letter))
	# return ''.join(l)
	return ''.join(map(calc, phrase))


def decrypt(phrase: str) -> str:
	# l = []
	# for letter in phrase:
	# 	l.append(calc(letter, 'decrypt'))
	# return ''.join(l)
	return ''.join(map(dec, phrase))


# e = encrypt('fox')
e = encrypt('look')
print(e)
d = decrypt(e)
print(d)