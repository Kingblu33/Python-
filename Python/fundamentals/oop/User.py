class user:
    def __init__(self, name):
        self.name = name
        self.amount = 0

    def make_withdrawl(self,amount):
        self.amount-=amount

    def make_deposit(self, amount):
        self.amount += amount
        print(self.amount)
        return self
    def display_user_balance(self): 
        print(f"User: {self.name} Balance: {self.amount} ")
    def transfer_method(self,amount,person):
        self.amount -= amount
        person.amount += amount

        self.display_user_balance()
        person.display_user_balance()

demmar= user("Demmar Allen")
blue= user("Monkey D luffy")
purple=user("Gol D Roger")
demmar.make_deposit(5000),demmar.make_deposit(2000),demmar.make_deposit(1000)
demmar.make_withdrawl(2000)
demmar.display_user_balance()

blue.make_deposit(2000),blue.make_deposit(1000)
blue.make_withdrawl(500),blue.make_withdrawl(500)
blue.display_user_balance()

purple.make_deposit(10000)
purple.make_withdrawl(300),purple.make_withdrawl(300),purple.make_withdrawl(300)
purple.display_user_balance()



demmar.transfer_method(1000,purple)