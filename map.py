from random import randrange
from Enemies import *
from Character import *


#Ships and enemies
ShipOneEnemies = [SimpleEnemy("a Deadly Rabbit", 20, 5), SimpleEnemy("a Ferocious Rat", 10, 15), SimpleEnemy("a Big Seagull", 15, 10)]
ShipOneDictionary = {
    "Enemies": ShipOneEnemies,
    "weaponloot" : Weapon("Pointy Stick", 2)
}


ShipTwoEnemies = [SimpleEnemy("a Spooky Scary Skeleton", 5, 20), SimpleEnemy("a Cool Cat", 7, 10), SimpleEnemy("an Octopus", 15, 20)]

ShipTwoDictionary = {
    "Enemies": ShipTwoEnemies,
    "weaponloot": Weapon("Very Pointy Stick", 3)
}

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

Loot_table = {"ShipOneEnemies": ShipOneDictionary,
              "ShipTwoEnemies": ShipTwoDictionary,
              "ShipThreeEnemies": ShipThreeDictionary
              }

