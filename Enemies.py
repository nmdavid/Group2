from random import randrange

class SimpleEnemy:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage

    def takeDamage(self, amount):
        self.health -= amount

    def doDamage(self):
        return randrange(0, self.damage)
