"""
Faça um Programa que leia um vetor de 5 números inteiros,
mostre a soma, a multiplicação e os números.

"""


vector = [1, 2, 3, 4, 5]


def calculate(vector):
	s = 0
	m = 0

	for num in vector:
		s += num
		m  = num * s
		print(num, s, m)


calculate(vector)
