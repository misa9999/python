class People:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age


class Customer(People):
    def __init__(self, name, age, account):
        super().__init__(name, age)
        self.__account = account


c1 = Customer("Misa", 25, 12345)
print(c1.name, c1.age)
