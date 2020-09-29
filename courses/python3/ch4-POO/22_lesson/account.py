from abc import ABC, abstractclassmethod


class Account(ABC):
    def __init__(self, agency, account_number, balance):
        self._agency = agency
        self._account_number = account_number
        self._balance = balance

    @property
    def agency(self):
        return self._agency

    @property
    def account_number(self):
        return self._account_number

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

    def details(self):
        print(f"Agency: {self.agency}", end=" ")
        print(f"Account: {self.account_number}", end=" ")
        print(f"Balance: {self.balance}")

    @abstractclassmethod
    def draw(self):
        pass


class AccountCC(Account):
    def __init__(self, agency, account_number, balance, limit):
        super().__init__(agency, account_number, balance)
        self._limit = limit

    @property
    def limit(self):
        return self._limit

    def draw(self, value):
        if (self.balance + self.limit) < value:
            print("Balance insufficient")
            return

        self.balance -= value


class AccountPP(Account):
    def draw(self, value):
        if self.balance < value:
            print("Balance insufficient")
            return

        self.balance -= value


cc = AccountCC(agency=11111, account_number=3333, balance=0, limit=500)
cc.deposit(100)
cc.details()
