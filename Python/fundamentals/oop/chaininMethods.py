class user:
    def __init__(self, name):
        self.name = name
        self.amount = 0

    def make_withdrawl(self,amount):
        self.amount-=amount
        return self

    def make_deposit(self, amount):
        self.amount += amount
        print(self.amount)
        return self
    def display_user_balance(self): 
        print(f"User: {self.name} Balance: {self.amount} ")
        return self
    def transfer_method(self,amount,person):
        self.amount -= amount
        person.amount += amount

        self.display_user_balance()
        person.display_user_balance()
        return self

demmar= user("Demmar Allen")
blue= user("Monkey D luffy")
purple=user("Gol D Roger")
demmar.make_deposit(5000).make_deposit(2000).make_deposit(1000).make_withdrawl(2000).display_user_balance()


blue.make_deposit(2000).make_deposit(1000).make_withdrawl(500).make_withdrawl(500) .display_user_balance()

purple.make_deposit(1000).make_withdrawl(300).make_withdrawl(300).display_user_balance()

demmar.transfer_method(1000,purple)