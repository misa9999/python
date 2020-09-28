import math


PI = math.pi


def double(list):
	return [x ** 2 for x in list]


def mul(list):
	r = 1
	for i in list:
		r *= i
	return r

if __name__ == '__main__':
	l1 = [1, 2, 3, 4, 5]
	print(double(l1))
	print(mul(l1))
	print(PI)


