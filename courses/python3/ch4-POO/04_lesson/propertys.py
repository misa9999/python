class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def discount(self, percentage):
        self.price = self.price - (self.price * percentage / 100)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value.title()
    # getter
    @property
    def price(self):
        return self._price
    # setter
    @price.setter
    def price(self, value):
        if isinstance(value, str):
            value = float(value.replace('U$', ''))

        self._price = value


p1 = Product('T-shirt', 50)
p1.discount(10)
print(p1.price)

p2 = Product('Mug', 'U$15')
p2.discount(10)
print(p2.price)

