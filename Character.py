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
        returnValue = "Your inventory contains the following: \n"
        for x in self.inventory:
            returnValue += "-%s : %s\n" % (x, self.inventory[x])
        return returnValue
        

    def printGear(self):
        returnValue = "You currently have equipped: \n"
        for g in self.armor:
            returnValue += "-%s, multiplies incoming damage by %d\n" %(g.name, g.armor)
        return returnValue

    def printWeapon(self):
        returnValue = "You wield the following: \n"
        for w in self.weapons:
            returnValue += "-%s, damage multiplier = %d\n" %(w.name, w.damage)
        return returnValue

    def doDamage(self):
        damage = self.damage
        for w in self.weapons:
            damage = damage * w.damage

    def takeDamage(self, amount):
        for g in self.armor:
            amount = amount * g.armor

    def printHealth(self):
        print("You are alive, you have: \n")
        return str(self.health) + " health"

    def consumePotion(self):
        if self.inventory["Health Potions"] >= 1:
            self.health += 30
            self.inventory["Health Potions"] -= 1
            return "Consumed potion! Health is now: " + str(self.health)
        else:
            return "No potions left!"
        

class Weapon:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

class Armor:
    def __init__(self, name, armor):
        self.name = name
        self.armor = armor
