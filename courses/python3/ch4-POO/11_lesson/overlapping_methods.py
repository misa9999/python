class People:
	def __init__(self, name, age):
		self.name = name
		self.age = age
		self.classname = self.__class__.__name__

	def speak(self):
		print(f'{self.classname} talking...')


class Customer(People):
	def buy(self):
		print(f'{self.classname} buying...')

	def speak(self):
		print('CUSTOMER')


class CustomerVIP(Customer):
	def __init__(self, name, age, last_name):
		# super().__init__(name, age)
		People.__init__(self, name, age)
		self.last_name = last_name

	def speak(self):
		# super().speak()
		People.speak(self)
		Customer.speak(self)
		print(f'{self.name} {self.last_name}')


c1 = Customer('Misa', 25)
c1.buy()

print()

c2 = CustomerVIP('Lucy', 20, 'Heartfilia')
c2.speak()
