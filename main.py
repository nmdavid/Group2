from map import *
from Character import *
from sys import exit
from gameparser import *
from story import *

ourHero = MainCharacter("Dave", 100, 20, 
                        {"Health Potions" : 1, "Artifacts": 0}, 
                        [Armor("Sailors pants", 1),],
                        [Weapon("Simple Dagger", 2),])
player_coordinates = [0,0]
run = True
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

def print_map(user_coordinates):
    grid = [["~","~","~","~","~","~","~","~","~","~"],["~","~","~","~","~","~","~","~","~","~"],["~","~","~","~","~","~","~","~","~","~"],["~","~","~","~","~","~","~","~","~","~"],["~","~","~","~","~","~","~","~","~","~"],["~","~","~","~","~","~","~","~","~","~"],["~","~","~","~","~","~","~","~","~","~"],["~","~","~","~","~","~","~","~","~","~"],["~","~","~","~","~","~","~","~","~","~"],["~","~","~","~","~","~","~","~","~","~"]]
    grid[user_coordinates[1]][user_coordinates[0]] = "⛵"
    print("\n\n\n\n\n")
    for column in grid:
        line = '    '.join(column)
        print(line+"\n")

def move_player(direction, user_coordinates):
    if direction == "north" and (user_coordinates[1]-1) >= 0:
        user_coordinates[1] -= 1
        return user_coordinates
    elif direction == "south" and (user_coordinates[1]+1) <= 9:
        user_coordinates[1] += 1
        return user_coordinates
    elif direction == "east" and (user_coordinates[0]+1) <= 9:
        user_coordinates[0] += 1
        return user_coordinates
    elif direction == "west" and (user_coordinates[0]-1) >= 0:
        user_coordinates[0] -= 1
        return user_coordinates
    else:
        print("Cannot sail that way.\n")
    
    
## main game loop
def main():
    startMenu()
       

def startMenu():
    global run
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
        choice = normalise_input(choice)
        choice = "".join(choice)
        if choice == "start":
            startGame()
            run = False
        elif choice == "credits":
            rollCredits()
        elif choice == "exit":
            print("\nThank you for playing!")
            run = False


def startGame():
    printIntro()
    mainGameLoop()

def mainGameLoop():
    global player_coordinates # I'll make this more elegant later
    global run
    while run:
        oldCoordinates = player_coordinates
        overWorld()
        if player_coordinates != oldCoordinates:
            enterZone()

def overWorld():
    global player_coordinates
    global run
    global ourHero
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print_map(player_coordinates)

    directions = ""
    if(player_coordinates[1] > 0): directions += "north, "
    if(player_coordinates[0] > 0): directions += "west, "
    if(player_coordinates[1] < 9): directions += "south, "
    if(player_coordinates[0] < 9): directions += "east, "
 
    print("You can:\n-Go %s\n-Check inventory\n-Check gear\n-Check weapons\n-Exit\n" % directions)
    player_input = input("What would you like to do?\n>")
    player_input = normalise_input(player_input)

    if player_input[0] == "check" and len(player_input) > 1:
        if player_input[1] == "inventory":
            displayMessage(ourHero.printInventory())
        elif player_input[1] == "gear":
            displayMessage(ourHero.printGear())
        elif player_input[1] == "weapons":
            displayMessage(ourHero.printWeapon())
    elif player_input[0] == "go":
        player_coordinates = move_player(player_input[1], player_coordinates)
    elif player_input[0] == "exit":
        run = False

def enterZone():
    global player_coordinates

def displayMessage(text):
    print(text)
    input("Enter anything to return to previous menu")

def rollCredits():
    print("Game created by:")

def battlePhase(enemies):
    for e in enemies:
        print("%s does %d damage!" % (e.name, e.doDamage()))

main()
