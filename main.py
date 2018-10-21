from map import *
from Character import *

ourHero = MainCharacter("Dave", 100, 20, {"Health Potions" : 3, "Gold": 7}, 
                        [Armor("Sailors pants", 5)],
                        [Weapon("Simple Dagger", 5)]) 

#Game logic
def player_change_location():
    print("Available ships:")
    for x in Ships:
        print("-" + x["name"])
    print("Where would you want to go?")
    name = input()
    for x in Ships:
        if x["name"] == name:
            current_ship = x
            return current_ship


def encounter():
    print("Meh")
        
    
## main game loop
def main():
    startMenu()
    current_ship = player_change_location()
    print(current_ship["description"])
    battlePhase(current_ship["Enemies"])
        

def startMenu():
    run = True

    while(run == True):
        print("########################################")
        print("|      Pirates of the Dark Seas        |")
        print("#======================================#")
        print("|            Main Menu:                |")
        print("#--------------------------------------#")
        print("|              Start                   |")
        print("|             Credits                  |")
        print("|              Exit                    |")
        print("#======================================#")
        print("Please enter your choice:")

        choice = input()
        if choice == "Start":
            startGame()
            run = False
        elif choice == "Credits":
            rollCredits()
            run = False
        elif choice == "Exit":
            run = False

    exit()

def startGame():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    ourHero.printInventory()

def rollCredits():
    print("Game created by:")

def battlePhase(enemies):
    for e in enemies:
        print("%s does %d damage!" % (e.name, e.doDamage()))
main()
