from map import *
from Character import *
from sys import exit
from gameparser import *
from story import *
import random

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


def encounter(difficulty):
    global ourHero
    enemies = []
    reward = 0
    if difficulty == "easy":
        enemies = ShipOneEnemies
        reward = 0
    if difficulty == "medium":
        enemies = ShipTwoEnemies
        reward = 1
    if difficulty == "hard":
        enemies = ShipThreeEnemies
        reward = 2
    enemy = enemies[random.randint(0,1)]
    while True:
        print("\nYou are fighting a "+enemy.name)
        print("You have "+str(ourHero.health)+" HP.")
        print("The "+enemy.name+" has "+str(enemy.health)+" HP.")
        choice = input("You can:\nFight\nHeal\nWhat do you want to do?\n>")
        if choice == "heal" and ourHero.inventory["Health Potions"] > 0:
            ourHero.inventory["Health Potions"] -= 1
            ourHero.health += 50
            if ourHero.health >= 100:
                ourHero.health = 100
            print("\nYou drank a healing potion.")
        elif choice == "fight":
            crit = random.randint(1,20)
            damage = ourHero.doDamage()
            if crit == 0:
                print("You missed!")
            elif crit != 0 and crit != 20:
                enemy.health -= damage
                print("\nYou hit the "+enemy.name+" for "+str(damage)+" damage.")
            elif crit == 20:
                enemy.health -= (damage*2)
                print("\nYou hit the "+enemy.name+" for "+str(damage*2)+" damage. Critical hit!")
        else:
            print("\nYou can't do that now.")
        if ourHero.health <= 0:
            print("\nYou died! The treasure will stay hidden forever...")
            sys.exit()
        if enemy.health <= 0:
            print("\nYou defeated the "+enemy.name+"!")
            ourHero.inventory["Health Potions"] += reward
            break
        enemy_damage = ourHero.takeDamage(enemy.doDamage())
        ourHero.health -= enemy_damage
        print("\nYou were hit for "+str(enemy_damage)+" damage.")          
            
        

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

def riddle():
    riddles = {"With one simple action, how do you make a pirate angry?": [1, "Take the p away", "Kill his parrot", "Throw water at him", "Steal his treasure"],
               "A pirate ransacks a village, but their treasure chest is locked. The pirate demands the code for the combination lock, the mayor says that the code is random everyday and if anyone in the village is hurt then he will never get the code. The pirate guesses the code – how?": [3,"He smashes the lock", "The code was 0000", "The code was random","The code was 1234"],
               "A pirate should always have a tip-top compass, but this pirates has been weather worn by the salty sea air, and now only shows the norm. What does it show?": [3, "N", "Nothing", "N, E, S, W", "N, NE, E, SE, S, SW, W, NW"],
               "After crossing a magical island, a pirate reaches the ancient tomb where the guardian ghost tells him that there are three passages to take through the cave to reach the treasure at the other end. The first passage has cannons in the walls that will fire randomly, the second passage has trained ancient warrior guards and the third has lions who haven’t eaten for 2 years. Which passage should the pirate take?": [3,"1","2","3","None of them"],
               "A pirate needs it when they throw it away, but brings it back when they don’t. What is it?": [3,"A ship", "The sea", "An anchor", "A parrot"],
               "Pirates sail the world going from island to island, and continent to continent. Australia is the world’s largest island – but before it was discovered what was the largest island in the world?": [4, "Madagascar", "Jamaica", "Great Britain", "Australia"],
               "A pirate shoots her parrot, then holds the parrot under water for 5 minutes. Later she feeds her parrot a cracker and they stare out across the sea together. How?": [4, "It was all a dream", "She has two parrots", "She fed a dead parrot and then held up its body", "The pirate took a picture of the parrot and developed it"],
               "Roger’s pirate father has three sons: Bluebeard, Greybeard and ...?": [3, "Kirill", "Blackbeard", "Roger", "Redbeard"],
               "What four letter starts with wind?": [1,"Ship", "Wind", "Seas", "Coin"],
               "A pirate just left her favourite rum shack in Barbados, but she left something behind. She does however always have this something too. What did she leave?": [4, "Money", "Alcoholism", "Rum", "Fingerprints"]
               }
    riddle_select = random.randint(0,9)
    riddle = list(riddles.keys())[riddle_select]
    answers = list(riddles.values())[riddle_select]
    answer = answers[0]
    attempts = 0
    while attempts < 3:
        print("\n"+riddle)
        print("\nA: "+answers[1]+"\nB: "+answers[2]+"\nC: "+answers[3]+"\nD: "+answers[4])
        print("\nYou have "+str(3-attempts)+" attempts left.\n")
        player_answer = input(">")
        player_answer = normalise_answer(player_answer)
        if player_answer[0] == "a" and answer == 1:
            print("Correct!")
            return True
        elif player_answer[0] == "b" and answer == 2:
            print("Correct!")
            return True
        elif player_answer[0] == "c" and answer == 3:
            print("Correct!")
            return True
        elif player_answer[0] == "d" and answer == 4:
            print("Correct!")
            return True
        else:
            print("Incorrect.")
            attempts += 1
    print("You got the riddle wrong!")
    return False

def printIntro():
    print("""\n\n\n\n\nWaking up on the shore of a lonely island, you barely retain the memories of your escape
from the cruel pirate prison. As you look to your new surroundings, you see the
lifeless bodies of two of your companions. Mourning their loss, you decide to give them a
true burial. As you drag one body through the sand a bottle containing some
battered parchment falls from his pocket. you uncork the bottle and read the letter inside.
    _____                                                          ______
   /     \________________________________________________________/      \
  / \                                                                     \
  |  |                                                                    |
   \ /___________________________________________________________________/
    \                                                                  |
    |    For ye who follow,                                            |
    |                                                                  |
    |    I be dead now, which means I must pass my legacy to           |
    |    another who shall retain the objects better than I.           |
    |    Far across the crystal waves scattered are artefacts          |
    |    of no one price. These six objects shall lead ye to         /
    |    the final pass where the treasure I horded over decades      |
    /    shall lay waiting for the arrival of one worthy. Go.         |
    |    Claim what belongs to the oceans now, but be wary. This      |
    |    is no task for a yellow-bellied bilge rat.                   |
    \                                                                 |
     |   Farewell and good fortune,                                   /
     |   Hack Narrow                                                 /
    /                                                               |
   /  ____ _____________________________________________________________                                                       
   | /    \                                                             \
   \ \__  |                                                              |
    \____/______________________________________________________________/


You find a small sailing vessel abandoned on the beach, and set out to find the artefacts that the scroll mentions.
    """)
    input("Press Enter to continue.")
                                                                                       

                                                        

    
## main game loop
def main():
    startMenu()
       

def startMenu():
    global run
    while(run == True):
        print("########################################")
        print("|                                      |")
        print("|    The Pirates of the Approximate    |")
        print("|    Atlantic and The Curse of The     |")
        print("|          Ancient Artefacts           |")
        print("|                                      |")
        print("#======================================#")
        print("|             Main Menu:               |")
        print("#--------------------------------------#")
        print("|               Start                  |")
        print("|              Credits                 |")
        print("|               Exit                   |")
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
    global player_coordinates
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
 
    print("You can:\n-Go %s\n-Check inventory\n-Check gear\n-Check weapons\n-Check health\n-Exit\n" % directions)
    player_input = input("What would you like to do?\n>")
    player_input = normalise_input(player_input)

    if player_input[0] == "check" and len(player_input) > 1:
        if player_input[1] == "inventory":
            displayMessage(ourHero.printInventory())
        elif player_input[1] == "gear":
            displayMessage(ourHero.printGear())
        elif player_input[1] == "weapons":
            displayMessage(ourHero.printWeapon())
        elif player_input[1] == "health":
            displayMessage(ourHero.printHealth())
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

encounter("easy")
encounter("medium")
encounter("hard")
main()
