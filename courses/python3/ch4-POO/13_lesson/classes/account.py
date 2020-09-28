from abc import ABC, abstractmethod


class Account(ABC):
    def __init__(self, agency, account, balance):
        self._agency = agency
        self._account = account
        self._balance = balance

    @property
    def agency(self):
        return self._agency

    @property
    def account(self):
        return self._account

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("Just numbers")

        self._balance = value

    def deposit(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("Just numbers")

        self.balance += value
        self.details()

    def details(self):
        print(f'Agency: {self.agency}', end=' ')
        print(f'Account: {self.account}', end=' ')
        print(f'Balance: {self.balance}')

    @abstractmethod
    def draw(self, value):
        pass
