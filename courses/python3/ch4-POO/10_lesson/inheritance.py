    """
association - use | aggregation - has | composition - Is owner | inheritance IS
"""


class People:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.classname = self.__class__.__name__

    def speak(self, subject):
        print(f'CLASS: {self.classname}')
        print(f'{self.name} is talking about {subject}')


class Customer(People):
    def buy(self):
        print(f'{self.classname} buying...')


class Student(People):
    def to_study(self):
        print(f'{self.classname} studying...')


c1 = Customer('misa', 25)
c1.speak('ice cream')
c1.buy()

s1 = Student('lucy', 20)
s1.speak('cookie')
s1.to_study()
