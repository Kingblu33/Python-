class BankAccount:
    bankname= "Scams Are us"
    all_accounts=[]
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance= balance
        BankAccount.all_accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        self.balance -= amount
        return self

    def display_account_info(self): 
        print(f"Balance: {self.balance}")
        return self

    def yield_interest(self):
        temp = self.balance * self.int_rate
        self.balance+=temp
        return self

    @classmethod
    def all_balances(cls):

        for account in cls.all_accounts:
            print(f"Balance: {account.balance}")
        return sum

account1= BankAccount(0.01,600)
account2= BankAccount(0.01,500)

account1.deposit(200).deposit(200).withdraw(50).withdraw(45).withdraw(25).yield_interest().display_account_info()
account2.deposit(200).deposit(300) .withdraw(200).withdraw(20).withdraw(20).withdraw(20).yield_interest().display_account_info()

BankAccount.all_balances()