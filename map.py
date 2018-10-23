from random import randrange
from Enemies import *
from Character import *


#Ships and enemies
ShipOneEnemies = [SimpleEnemy("Deadly Rabbit", 20, 5), SimpleEnemy("Ferocious Rat", 10, 15)]
ShipOneDictionary = {
    "name": "Madman",
    "Enemies": ShipOneEnemies,
    "Gold": 100,
    "description": "A very cool ship",
    "weaponloot" : Weapon("Biggie", 1000000)
}


ShipTwoEnemies = [SimpleEnemy("Spooky Scary Skeleton", 5, 20), SimpleEnemy("Cool Cat", 7, 10)]

ShipTwoDictionary = {
    "name": "The ship of death",
    "Enemies": ShipTwoEnemies,
    "Gold": 300,
    "description": "This ship cooler tho",
    "weaponloot": Weapon("Flintlock pistol", 5)
}

ShipThreeEnemies = [SimpleEnemy("Angry Pirate", 35, 10), SimpleEnemy("Very Angry Pirate", 45, 12)]
ShipThreeDictionary = {
    "name": "The ship of death",
    "Enemies": ShipThreeEnemies,
    "Gold": 300,
    "description": "This ship cooler tho",
    "weaponloot": Weapon("Pointy stick", 3)
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

