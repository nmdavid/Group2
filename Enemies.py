from random import randrange

class SimpleEnemy: #This class is used to create the different enemies
    def __init__(self, name, health, damage): #Builder function
        self.name = name
        self.health = health
        self.damage = damage

    def takeDamage(self, amount): #Function used for enemies to take damage
        self.health -= amount

    def doDamage(self): #Function used for enemies to deal damage
        return randrange(0, self.damage)
