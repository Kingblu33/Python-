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
        return f"Balance:{self.balance}"

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


class user:
    def __init__(self, name, savings ,checkings):
        self.name = name
        self.account= BankAccount(0.01,0)
        self.savings = savings
        self.checkings = checkings

    def display_user_balance(self): 
        print(f"User: {self.name} {self.account.display_account_info()} ")

    def transfer_method(self,amount,person):
        self.amount -= amount
        person.amount += amount
        self.display_user_balance()
        person.display_user_balance()

    def deposit_savings(self,save):
        self.savings =+ save

    def deposit_checkings(self,check):
        self.checkings += check
        return self

    def savingsandcheck(self):
        print(f"Amount in checking {self.checkings}, Amount in savings:{self.savings}")
        return self

demmar = user("Demmar Allen",0,0)
demmar.account.deposit(3000)
demmar.display_user_balance()
demmar.deposit_checkings(1000).deposit_savings(2000)
demmar.savingsandcheck()

