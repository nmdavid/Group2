from random import randrange
from Enemies import *
from Character import *


#Ships and enemies

#Enemies are grouped into "ships" where enemies of similar difficulty are on the same "ship"
#Ships also have weapons as loot scaled to the difficulty of the enemies

#These are the "easy" enemies and loot
ShipOneEnemies = [SimpleEnemy("a Deadly Rabbit", 25, 10), SimpleEnemy("a Ferocious Rat", 28, 11), SimpleEnemy("a Big Seagull", 35, 15)]
ShipOneDictionary = {
    "Enemies": ShipOneEnemies,
    "weaponloot" : Weapon("Pointy Stick", 2)
}

#These are the "medium" enemies and loot
ShipTwoEnemies = [SimpleEnemy("a Spooky Scary Skeleton", 33, 15), SimpleEnemy("a Cool Cat", 35, 17), SimpleEnemy("an Octopus", 40, 20)]
ShipTwoDictionary = {
    "Enemies": ShipTwoEnemies,
    "weaponloot": Weapon("Very Pointy Stick", 3)
}

#These are the "hard" enemies and loot
ShipThreeEnemies = [SimpleEnemy("an Angry Pirate", 40, 30), SimpleEnemy("a Very Angry Pirate", 45, 35), SimpleEnemy("Captain Kirill", 55, 45)]
ShipThreeDictionary = {
    "Enemies": ShipThreeEnemies,
    "weaponloot": Weapon("Flintlock Pistol", 5)
}

#List of rooms
Ships = [
    ShipOneDictionary,
    ShipTwoDictionary
]
#This is used to find the loot based on which enemy appeared in the encounter
Loot_table = {"ShipOneEnemies": ShipOneDictionary,
              "ShipTwoEnemies": ShipTwoDictionary,
              "ShipThreeEnemies": ShipThreeDictionary
              }

