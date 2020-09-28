class Customer:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.address = []

    def insert_address(self, city, state):
        self.address.append(Address(city, state))

    def show_address(self):
        for address in self.address:
            print(address.city, address.state)

    def __del__(self):
        print(f'{self.name} has been deleted')


class Address:
    def __init__(self, city, state):
        self.city = city
        self.state = state

    def __del__(self):
        print(f'{self.city}/{self.state} has been deleted')


c1 = Customer('misa', 25)
c1.insert_address('Belo Horizonte', 'MG')
print(c1.name)
c1.show_address()
del c1
print()

c2 = Customer('lucy', 20)
print(c2.name)
c2.insert_address('São Paulo', 'SP')
c2.insert_address('Rio de Janeiro', 'RJ')
c2.show_address()
del c2
print()

c3 = Customer('megumin', 16)
print(c3.name)
c3.insert_address('Manaus', 'Amazonas')
c3.insert_address('Bahia', 'BA')
c3.insert_address('Goiania', 'GO')
c3.show_address()
del c3
print()

print('#####################################')
