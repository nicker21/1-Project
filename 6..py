class Robot :
    name ="Bob"
    color ="green"

    def __unit__(self,agility,strength,power):
        self.agility = agility
        self.strength = strength
        self.power = power

    def noise (self) :
        print("Fight !!")

    def eat(self):
        print("Ням ням")

    def go_back(self):
        print("come back")


class Atlas(Robot):
    def __init__(self, agility,strength,power,armor):
        super().__init__(agility,strength,power)
        self.armor = armor

    def Bounce (self):
        print("yuhooo")

class Handle(Robot):
    def __init__(self, agility, strength, power, armor,speed):
        super().__init__(agility, strength, power,armor)
        self.speed = speed


    def Help(self):
        print("Do you need help ?")







