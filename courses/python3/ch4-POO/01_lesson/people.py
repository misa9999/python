from datetime import datetime


class People:
	current_year = int(datetime.strftime(datetime.now(), '%Y'))

	def __init__(self, name, age, eating=False, speaking=False):
		self.name = name
		self.age = age
		self.eating = eating
		self.speaking = speaking

		# variable = 'value'

	def show_info(self):
		print(f'Name: {self.name} | age: {self.age}')

	def eat(self, food):
		if self.eating:
			print(f'{self.name} is already eating.')
			return

		if self.speaking:
			print(f"{self.name} can't eat talking")
			return

		print(f'{self.name} is eating {food}')
		self.eating = True

	def stop_eating(self):
		if not self.eating:
			print(f"{self.name} isn't eating")
			return

		print(f'{self.name} stopped eating')
		self.eating = False

	def speak(self, subject):
		if self.eating:
			print(f"{self.name} can't talk eating.")
			return

		if self.speaking:
			print(f"{self.name} is already talking.")
			return

		print(f'{self.name} is talking about {subject}')
		self.speaking = True

	def stop_talking(self):
		if not self.speaking:
			print(f"{self.name} isn't talking.")
			return

		print(f"{self.name} stopped talking")
		self.speaking = False

	def get_year_birth(self):
		return self.current_year - self.age
