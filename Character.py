from random import randrange
from random import randint
class MainCharacter: #This is the class used for the player character
    def __init__(self, name, health, damage, inventory, armor, weapons): #Builder function
        self.name = name
        self.maxHealth = self.health = health
        self.damage = damage
        self.inventory = inventory
        self.armor = armor
        self.weapons = weapons

    def printInventory(self): #Function that lets the player's inventory be read and displayed
        returnValue = "Your inventory contains the following: \n"
        for x in self.inventory:
            returnValue += "-%s : %s\n" % (x, self.inventory[x])
        return returnValue
        

    def printGear(self): #Function that lets the player's armor be read and displayed
        returnValue = "You currently have equipped: \n"
        for g in self.armor:
            returnValue += "-%s, reduces incoming damage by %d\n" %(g.name, g.armor)
        return returnValue

    def printWeapon(self): #Function that lets the player's weapons be read and displayed
        returnValue = "You wield the following: \n"
        for w in self.weapons:
            returnValue += "-%s, damage multiplier = %d\n" %(w.name, w.damage)
        return returnValue

    def doDamage(self): #Function for the player to deal damage to enemies
        damage = randint(1,self.damage)
        for w in self.weapons:
            damage = damage * w.damage
        return damage

    def takeDamage(self, amount): #Function for the player to take damage from enemies
        for g in self.armor:
            if amount > 0 and (amount-g.armor) >= 0:
                amount = amount - g.armor
        return int(amount)

    def printHealth(self): #Function that lets the player's health be read and displayed
        print("You are alive, you have: \n")
        return str(self.health) + " health"


        

class Weapon:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

class Armor:
    def __init__(self, name, armor):
        self.name = name
        self.armor = armor
