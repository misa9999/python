from abc import ABC, abstractmethod


class A(ABC):
    @abstractmethod
    def speak(self):
        pass


class B(A):
    def speak(self):
        print("talking... B...")


a = B()
a.speak()
