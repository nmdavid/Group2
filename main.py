from map import *
from Character import *
from sys import exit
from gameparser import *

ourHero = MainCharacter("Dave", 100, 20, {"Health Potions" : 3, "Gold": 7}, 
                        [Armor("Sailors pants", 5)],
                        [Weapon("Simple Dagger", 5)])
player_coordinates = [0,0]

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
        choice = normalise_input(choice)
        choice = "".join(choice)
        if choice == "start":
            startGame()
            run = False
        elif choice == "credits":
            rollCredits()
        elif choice == "exit":
            print("\nThank you for playing!")
            sys.exit()


def startGame():
    global player_coordinates # I'll make this more elegant later
    while True:
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print_map(player_coordinates)
        print("You can:\nGO NORTH/SOUTH/EAST/WEST\nCHECK INVENTORY\n")
        player_input = input("What would you like to do?\n>")
        player_input = normalise_input(player_input)
        if player_input[0] == "check" and player_input[1] == "inventory":
            ourHero.printInventory()
        elif player_input[0] == "go":
            player_coordinates = move_player(player_input[1], player_coordinates)

def rollCredits():
    print("Game created by:")

def battlePhase(enemies):
    for e in enemies:
        print("%s does %d damage!" % (e.name, e.doDamage()))
main()
