from random import randrange
from Enemies import *
from Character import *


#Ships and enemies

#Enemies are grouped into "ships" where enemies of similar difficulty are on the same "ship"
#Ships also have weapons as loot scaled to the difficulty of the enemies

#These are the "easy" enemies and loot
ShipOneEnemies = [SimpleEnemy("a Deadly Rabbit", 20, 5), SimpleEnemy("a Ferocious Rat", 10, 15), SimpleEnemy("a Big Seagull", 15, 10)]
ShipOneDictionary = {
    "Enemies": ShipOneEnemies,
    "weaponloot" : Weapon("Pointy Stick", 2)
}

#These are the "medium" enemies and loot
ShipTwoEnemies = [SimpleEnemy("a Spooky Scary Skeleton", 5, 20), SimpleEnemy("a Cool Cat", 7, 10), SimpleEnemy("an Octopus", 15, 20)]
ShipTwoDictionary = {
    "Enemies": ShipTwoEnemies,
    "weaponloot": Weapon("Very Pointy Stick", 3)
}

#These are the "hard" enemies and loot
ShipThreeEnemies = [SimpleEnemy("an Angry Pirate", 35, 10), SimpleEnemy("a Very Angry Pirate", 45, 12), SimpleEnemy("Captain Kirill", 55, 15)]
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

