import dojopets

class Ninja():
    def __init__(self,first_name,last_name, treats, pet_food,pet):
        self.first_name= first_name
        self.last_name= last_name
        self.treats= treats
        self.pet_food=pet_food
        self.pet= pet
    
    def ash(self):
        print(f"Pet Owner: {self.first_name} {self.last_name}")
        return self
    def walk(self):
        self.pet.play()
        return self

# return self

    def feed(self):
        self.pet.eat()
        return self 

    def bathe(self):
        self.pet.noise()
        return self

nen= Ninja("Ash","Ketchum","bis","meat",dojopets.pickachu)
nen.ash()
dojopets.pickachu.showname()
nen.walk().feed().bathe()




