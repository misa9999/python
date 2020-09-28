from classes.account import Account


class SavingsAccount(Account):
    def draw(self, value):
        if self.balance < value:
            print('Balance insufficient')
            return

        self.balance -= value
        self.details()
