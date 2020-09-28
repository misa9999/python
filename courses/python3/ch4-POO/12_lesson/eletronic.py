class Eletronic:
	def __init__(self, name):
		self._name = name
		self._turned_on = False

	def turn_on(self):
		if self._turned_on:
			return

		self._turned_on = True

	def turn_off(self):
		if not self._turned_on:
			return

		self._turned_on = False
