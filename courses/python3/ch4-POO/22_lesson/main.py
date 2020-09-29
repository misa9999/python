"""
Exercício com Abstração, Herança, Encapsulamento e Polimorfismo
Criar um sistema bancário (extremamente simples) que tem clientes, contas e
um banco. A ideia é que o cliente tenha uma conta (poupança ou corrente) e que
possa sacar/depositar nessa conta. Contas corrente tem um limite extra. Banco
tem clientes e contas.

Dicas:
Criar classe Cliente que herda da classe Pessoa (Herança)
    Pessoa tem nome e idade (com getters)
    Cliente TEM conta (Agregação da classe ContaCorrente ou ContaPoupanca)
Criar classes ContaPoupanca e ContaCorrente que herdam de Conta
    ContaCorrente deve ter um limite extra
    Contas têm agência, número da conta e saldo
    Contas devem ter método para depósito
    Conta (super classe) deve ter o método sacar abstrato (Abstração e
    polimorfismo - as subclasses que implementam o método sacar)
Criar classe Banco para AGREGAR classes de clientes e de contas (Agregação)
Banco será responsável autenticar o cliente e as contas da seguinte maneira:
    Banco tem contas e clentes (Agregação)
    * Checar se a agência é daquele banco
    * Checar se o cliente é daquele banco
    * Checar se a conta é daquele banco
Só será possível sacar se passar na autenticação do banco (descrita acima)
"""
from bank import Bank
from client import Client
from account import AccountCC, AccountPP

bank = Bank()

client1 = Client("Misa", 25)
client2 = Client("Lucy", 20)
client3 = Client("Asuna", 18)

account1 = AccountPP(agency=1111, account_number=254136, balance=0)
account2 = AccountCC(agency=2222, account_number=321453, balance=0, limit=500)
account3 = AccountPP(agency=1422, account_number=221355, balance=0)

client1.insert_account(account1)
client2.insert_account(account2)
client3.insert_account(account3)

bank.insert_client(client1)
bank.insert_account(account1)

if bank.authenticate(client1):
    client1.account.deposit(100)
    client1.account.draw(30)
else:
    print("Unkown client")

print("####################")

if bank.authenticate(client2):
    client2.account.deposit(100)
    client2.account.draw(30)
else:
    print("Unkown client")
