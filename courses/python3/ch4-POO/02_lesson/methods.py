class People:
	curret_year = 2020

	def __init__(self, name, age):
		self.name = name
		self.age = age

	def get_year_birth(self):
		print(self.curret_year - self.age)

	@classmethod
	def by_year_birth(cls, name, year_birth):
		age = cls.curret_year - year_birth
		return cls(name, age)


# p1 = People('Misa', 26)
p1 = People.by_year_birth('Misa', 1994)
print(p1)
print(p1.name, p1.age)
p1.get_year_birth()
