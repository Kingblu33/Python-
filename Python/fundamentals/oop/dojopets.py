class Pet():
    def __init__(self,name,type,tricks):
        self.name= name
        self.type=type
        self.tricks=tricks
        self.health= 70
        self.energy=70
    def showname(self):
        print(f"Pet Name: {self.name}")
    def sleep(self):
        self.energy+= 25
        return self

    def eat(self):
        self.energy += 5 
        self.health+= 10
        print(f"Energy after eating:{self.energy} Health after: {self.health}")
        return self


    def play(self):
        self.health+= 5
        print(self.health)
        return self

    def noise(self):
        print("Animal purrs")
        return self

pickachu= Pet("Pickachu","Electric","lightning bolt")



