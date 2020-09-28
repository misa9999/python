from classes.cp import SavingsAccount
from classes.cc import CurrentAccount


sa = SavingsAccount(1111, 1111, 11)
sa.deposit(10)
sa.draw(5)
sa.draw(5)
sa.draw(5)
sa.draw(5)
sa.draw(5)

print('#################################')
cc = CurrentAccount(agency=11111, account=3333, balance=0, limit=500)
cc.deposit(100)
cc.draw(250)
cc.draw(500)
cc.deposit(1000)
