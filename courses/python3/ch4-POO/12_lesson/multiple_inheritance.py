class A:
	def speak(self):
		print('Talking... Im in A.')


class B(A):
	def speak(self):
		print('Talking... Im in B.')


class C(A):
	def speak(self):
		print('Talking... Im in C.')


class D(B, C):
	pass


d = D()
d.speak()
