from random import randrange
from Enemies import *

CharacterInventory = {
    "Sword":1,
    "Shield":2,
    "Gold": 0,
    "HealthPotion":3
}
CharacterDictionary = {
    "Name": "Dave the Conqueror",
    "MaxHealth": 100,
    "CurrentHealth": 100,
    "Strength": 5,
    "Armor": 10,
    "Inventory": CharacterInventory
}


#Ships and enemies
ShipOneEnemies = [SimpleEnemy("Deadly Rabbit", 20, 5), SimpleEnemy("Ferocious Rat", 10, 15)]
ShipOneDictionary = {
    "name": "Madman",
    "Enemies": ShipOneEnemies,
    "Gold": 100,
    "description": "A very cool ship" 
}


ShipTwoEnemies = [SimpleEnemy("Spooky Scary Skeleton", 5, 20), SimpleEnemy("Cool Cat", 7, 10)]

ShipTwoDictionary = {
    "name": "The ship of death",
    "Enemies": ShipTwoEnemies,
    "Gold": 300,
    "description": "This ship cooler tho"
}

ShipThreeEnemies = [SimpleEnemy("Angry Pirate", 35, 10), SimpleEnemy("Very Angry Pirate", 45, 12)]

#List of rooms
Ships = [
    ShipOneDictionary,
    ShipTwoDictionary
]

