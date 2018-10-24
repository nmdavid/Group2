from random import randrange
from Enemies import *
from Character import *


#Ships and enemies
ShipOneEnemies = [SimpleEnemy("Deadly Rabbit", 20, 5), SimpleEnemy("Ferocious Rat", 10, 15)]
ShipOneDictionary = {
    "Enemies": ShipOneEnemies,
    "weaponloot" : Weapon("Pointy Stick", 2)
}


ShipTwoEnemies = [SimpleEnemy("Spooky Scary Skeleton", 5, 20), SimpleEnemy("Cool Cat", 7, 10)]

ShipTwoDictionary = {
    "Enemies": ShipTwoEnemies,
    "weaponloot": Weapon("Very Pointy Stick", 3)
}

ShipThreeEnemies = [SimpleEnemy("Angry Pirate", 35, 10), SimpleEnemy("Very Angry Pirate", 45, 12)]
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

