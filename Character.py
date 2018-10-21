from random import randrange
class MainCharacter:
    def __init__(self, name, health, damage, inventory, armor, weapons):
        self.name = name
        self.maxHealth = self.health = health
        self.damage = damage
        self.inventory = inventory
        self.armor = armor
        self.weapons = weapons

    def printInventory(self):
        print("Your inventory contains the following: ")
        for x in self.inventory:
            print(x, ': ', self.inventory[x])



class Weapon:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

class Armor:
    def __init__(self, name, armor):
        self.name = name
        self.armor = armor
