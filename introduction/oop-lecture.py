
#OBJECT ORIENTED PROGRAMMING

#1. POLYMORPHISM (related to INHERITANCE)

#WHAT MAKES THEM DIFFERENT

#2. ENCAPSULATION (related to ABSTRACTION)

#PRIVATE INFO

#3. INHERITANCE

#HAVE SIMILILAR CLASSES IN COMMON 

#4. ABSTRACTION

# TAKE THE PRIVATE INFO (ENCAPSULATION) TO SHOW TO USER SIMPLE INFOS



class Fighter:
    def __init__(self, name, weapon, ability, strength, speed):
#       constructor
        #name, weapon, ability, strength, weight, speed, percent
        #print("Running the fighter constructor!")
        self.name = name
        self.weapon = weapon
        self.ability = ability
        self.strength = strength
        self.speed = speed
        self.percent = 0 
        self.sheilding = False

#Methods
    def printStatus(self):
        print(f"This is {self.name} all info:")
        print(f"name: {self.name}")
        print(f"weapon: {self.weapon}")
        print(f"ablitity: {self.ability}")
        print(f"strength: {self.strength}")
        print(f"speed: {self.speed}")


    def attack(self, opponent):
        if opponent.shielding:
            print(f"{opponent.name} has put up shield to block {self.name} attack")
            opponent.shielding = False
        else:
            damage = 6
            opponent.percent += damage
            print(f"{self.name} attacked {opponent.name} and dealt {damage}% !!!")

    def shield(self):
        self.sheilding = True
        print(f"{self.name} has put up their sheild!")




Sora = Fighter("Sora","Keyblade","Magic",8,17) #exp
#               name   weapon    ability strentgh and speed 

Kirby = Fighter("Kirby","none","mimick others ability",7,16) #exp

class Sora(Fighter):
    def __init__(self):
        print(f"Calling Sora constructor!")
        super().__init__("Sora","Keyblade","Magic",8,17)
        self.charged = False
    def special(self, opponant):
        if self.changed == True


Sora = sora

#print(Kirby.ability)
#print(Sora.weapon)


# Sora.attack(Kirby)
# Kirby.printStatus()
# Kirby.shield()


