from map import *
from Character import *
from sys import exit
from gameparser import *
from story import *
from random import *
from eventMap import *

ourHero = MainCharacter("Dave", 100, 5, 
                        {"Health Potions" : 1, "Artefacts": 0}, 
                        [Armor("Sailors pants", 1),],
                        [Weapon("Simple Dagger", 2), Weapon("Nothing", 1)])
player_coordinates = [0,0]
artefact_number = 0
run = True
#Game logic


def encounter(difficulty):
    global ourHero
    enemies = []
    reward = 0
    if difficulty == "easy":
        enemies = ShipOneEnemies
        loot_table = "ShipOneEnemies"
        reward = 0
    if difficulty == "medium":
        enemies = ShipTwoEnemies
        loot_table = "ShipTwoEnemies"
        reward = 1
    if difficulty == "hard":
        enemies = ShipThreeEnemies
        loot_table = "ShipThreeEnemies"
        reward = 2
    enemy = enemies[random.randint(0,1)]
    enemy_health = enemy.health
    print("\n\nYOU ENCOUNTER AN ENEMY!\n\n")
    while True:
        print("\nYou are fighting a "+enemy.name)
        print("You have "+str(ourHero.health)+" HP.")
        print("The "+enemy.name+" has "+str(enemy.health)+" HP.")
        choice = input("You can:\nFight\nHeal\nWhat do you want to do?\n>")
        if choice.lower() == "heal" and ourHero.inventory["Health Potions"] > 0:
            ourHero.inventory["Health Potions"] -= 1
            ourHero.health += 50
            if ourHero.health >= 100:
                ourHero.health = 100
            print("\nYou drank a healing potion.")
        elif choice.lower() == "fight":
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
            print("\n\nYou defeated the "+enemy.name+"!")
            ourHero.inventory["Health Potions"] += reward
            if reward > 0:
                print("\nYou found "+str(reward)+" Health Potions!\n")
            enemy.health = enemy_health
            battleEnded(Loot_table[loot_table])
            break
        enemy_damage = ourHero.takeDamage(enemy.doDamage())
        ourHero.health -= enemy_damage
        print("\nYou were hit for "+str(enemy_damage)+" damage.")          

def battleEnded(current_ship):
    loot_roll = random.randint(0,2)
    if loot_roll == 2:
        newWeapon = current_ship["weaponloot"]
        if len(ourHero.weapons) > 1:
            if ourHero.weapons[0].damage > ourHero.weapons[1].damage and newWeapon.damage > ourHero.weapons[1].damage:
                ourHero.weapons[1] = newWeapon
                print("\nYou got a new weapon, a "+newWeapon.name+"!")
            elif newWeapon.damage > ourHero.weapons[0].damage:
                ourHero.weapons[0] = newWeapon
                print("\nYou got a new weapon, a "+newWeapon.name+"!")
        else:
            ourHero.weapons[1] = newWeapon
   

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
        return user_coordinates

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
        if player_answer == []:
            print("Incorrect.")
            attempts += 1
        elif player_answer[0] == "a" and answer == 1:
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
                                                                                       
def get_artefact(artefact_number):
    artefacts = ["It's an old gold coin. Very old, and solid gold... \nIts value has no number that is for sure. The inscribed picture is a very stylised 'NE'.",
                 "This pot details the story of Perseus and medusa, an old Ancient Greek mythological story.\nOn the bottom is a ragged engraving, much newer in age.\nIt shows a skull, similar to the Jolly Roger.",
                 "This is a navigator's rutter. A logbook ofdirections, locations, maps and most importantly, directions to specific areas of the deadly ocean.\nThe directions point to an island on the southern edge of mapped ocean.\n",
                 "On a small island you find a flintlock pistol. This pistol is common amongst pirates and lawmen alike, containing a single shot. \nSeeing the unique leather wrapped handle reminds you of the owner, a friend from a life almost forgotten, living in Tortuga.",
                 "When you travel to find the old friend whose pistol you found,you discover he has retired to become a simple shop keep, who claims to know Hack Narrow, or at least he did... a long time ago. \nHe gives you a silver ring for your travels. On the inside are inscribed co-ordinates to a harbor town west of where the pot was.",
                 'The final artefact is held in a small museum in a quiet harbour town. \nYou go inside, and instantly one modest exhibit catches your eye. It is the figurehead piece of the famed ship, Silver Sword. \nIt is a solid silver model of a swordfish, with huge polished rubies for eyes. The item itself is immensely valuable, held behind thick glass and guarded by two armed men. \nIt seems somewhat out of place. You read the plaque in front of the exhibit. \n"The silver figurehead of the famed ship belonged to wealthy Spanish businessman Carlos Buendia... of course before it was stolen from him by the enigmatic band of pirates known as the black mist, \nand handed as a prize to their captain and leader Garton "No-Tongue" Crawford. It remained in his possession until death until it was passed into the possession of his equally infamous but outcast son, Hack Narrow. \nIt was in his period of possession where the ship was disassembled, the parts used to create some kind of storage room at a secret location, save this figurehead, donated to this museum."\n Shouting comes from outside the building, growing louder and louder until silenced with the crack of gunfire. \nThe guards rush out to investigate. You remove your acquired pistol from your jacket pocket, and use the single shot to shatter the glass surrounding the figurehead. \nApparently unnoticed due to the outside disturbance, you carefully remove the left ruby eye of the figurehead and search for an exit through the back of the museum. \nAs you walk away, you hear a group of men discussing something as they shuffle past the limp bodies of the guards into the museum. \n\nYou decide to travel away from the port.']
    print("\n\nYou found an artefact!\n")
    print(artefacts[artefact_number])
    artefact_number += 1
    ourHero.inventory["Artefacts"] += 1
    return artefact_number
    
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
        input("Press Enter to continue.")

def overWorld():
    global player_coordinates
    global run
    global ourHero
    global artefact_number
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print_map(player_coordinates)

    directions = ""
    if(player_coordinates[1] > 0): directions += "north, "
    if(player_coordinates[0] > 0): directions += "west, "
    if(player_coordinates[1] < 9): directions += "south, "
    if(player_coordinates[0] < 9): directions += "east, "
 
    print("You can:\n-Go %s\n-Check inventory\n-Check gear\n-Check weapons\n-Check health\n-Drink potion\n-Exit\n" % directions)
    player_input = input("What would you like to do?\n>")
    if player_input == "adminget":
        artefact_number += 1
    player_input = normalise_input(player_input)
    if player_input == []:
        pass
    elif player_input[0] == "check" and len(player_input) > 1:
        if player_input[1] == "inventory":
            displayMessage(ourHero.printInventory())
        elif player_input[1] == "gear":
            displayMessage(ourHero.printGear())
        elif player_input[1] == "weapons":
            displayMessage(ourHero.printWeapon())
        elif player_input[1] == "health":
            displayMessage(ourHero.printHealth())
    elif player_input[0] == "go" and len(player_input) > 1:
        player_coordinates = move_player(player_input[1], player_coordinates)
        event_checker(player_coordinates, event_map)
    elif player_input[0] == "exit":
        run = False
    elif player_input[0] == "drink" and player_input[1] == "potion" and ourHero.inventory["Health Potions"] > 0:
        ourHero.inventory["Health Potions"] -= 1
        ourHero.health += 50
        if ourHero.health >= 100:
            ourHero.health = 100
        print("\nYou drank a potion.\n")
    else:
        print("\nYou cannot do that.\n")

def enterZone():
    global player_coordinates

def displayMessage(text):
    print(text)

def rollCredits():
    print("\nGame created by:\n\nGROUP 2\n\nSara Abidi\nJake Casey\nNaomi Davidson\nJosh Fielding\nTommy Khalifa\nFinn Milliner\nRahul Singh\nJake Ziegler\n")

def battlePhase(enemies):
    for e in enemies:
        print("%s does %d damage!" % (e.name, e.doDamage()))

def event_checker(current_position, event_map):
    global artefact_number
    winchance = random.randint(1,4)
    if event_map[current_position[1]][current_position[0]] == 1:
        fight_event()
    elif event_map[current_position[1]][current_position[0]] == 2:
        riddle_event(hintlist)
    elif event_map[current_position[1]][current_position[0]] == 3:
        environment_event()
    elif event_map[current_position[1]][current_position[0]] == 4 and artefact_number == 1:
        artefact_number = get_artefact(artefact_number)
    elif event_map[current_position[1]][current_position[0]] == 5 and artefact_number == 3:
        artefact_number = get_artefact(artefact_number)
    elif event_map[current_position[1]][current_position[0]] == 6 and artefact_number == 4 :
        artefact_number = get_artefact(artefact_number)
    elif event_map[current_position[1]][current_position[0]] == 7 and artefact_number == 5 :
        artefact_number = get_artefact(artefact_number)
    elif artefact_number == 6 and winchance == 1:
        print('''You are sailing through calm seas and blue skies, the wind is present but not
strong. It is peaceful. You decide to look at the ruby eye, and see that it catches
the sunlight in a very unique manner. as you angle it differently, you see that it's
when pointed towards the ocean, the light casts red onto the waves. The next second a wave
hits and it's gone. You try find the same spot again, and find that it is a trail of red
being lit up by the ruby's reflection. You change the sails and follow the path, the
ruby lighting the way. The path finishes leading you into the mouth of a cave set just off
a crag of rocks. Your boat fits inside just, and not too far in, you find a short wooden
mooring dock. You step onto the rocky shore, following the tunnel into the cavern deeper.
After a short walk on wet rock, the walls and ceilings of the tunnel start to widen, and
the light seeping through small gaps in the rocks overhead reveal a small wooden door
just ahead. On the door is a small hole. A slot... a lock. It fits the shape of the ruby
perfectly as you push it into place and the door swings open. Revealed is a vast, high
ceilinged wooden structure, small windows of light keeping the contents barely visible.
What was visible, however, was a huge array of varied treasures, crowding the room entirely.
The room was filled to the wooden bowed ceilings by the golden, silver, crystal treasured
all piled together. A voice suddenly materialised from behind you, "So you found me, then".
''')
        print("\nYou win!")
        exit()
        

def fight_event():
    global artefact_number
    check = random.randint(1, 5)
    if check == 1:
        encounter("hard")
        if artefact_number == 2:
            get_chance = random.randint(1,2)
            if get_chance == 1:
                artefact_number = get_artefact(artefact_number)
    elif check == 2 or check == 3:
        encounter("medium")
    else:
        encounter("easy")
            
    if artefact_number == 0:
        get_chance = random.randint(1,3)
        if get_chance == 1:
            artefact_number = get_artefact(artefact_number)
    

def riddle_event(hintlist):
    global artefact_number
    global ourHero
    riddle_check = riddle()
    if riddle_check == True:
        print("\nHint:")
        print(hintlist[artefact_number])
    else:
        if ourHero.inventory["Health Potions"] > 0:
            ourHero.inventory["Health Potions"] -=1
            print("\nSorry, you lost a potion\n")
        elif ourHero.inventory["Health Potions"] == 0:
            print("\nYou still have 0 potions\n")



# Maybe add some actual affects of the environmental events? like loss of item, etc.
def environment_event():
    check = random.randint(1, 5)
    if check == 1:
        a = """
        A fin breaks the surface of the water infront of you,
        rising higher and higher out of the water the creature's immense
        size becomes quickly apparent as the jaws of a huge shark emerges
        opening wide, revealing row after row of sharp, jagged teeth.
        Just as it is about to reach your ship, it is dragged underneath.
        blood rises to the surface and a booming noise comes from below,
        deafening you completely.
        """
        print(a)
    elif check == 2:
        a = """
        Sharp scraping from underneath the deck wakes you from a daydream.
        you see the approaching water is somewhat darker then usual in spots.
        As you move over another dark spot you see it is a sharp crag of rock
        underneath the boat... you are moving into shallows.. in the middle of
        the ocean. You scramble to change course as each second here risks
        total destruction of the boat. Narrowly you escape from the field with
        nothing more than a small amount of damage on the underside of your ship.
        """
        print(a)
    elif check == 3:
        a = """
        Not too far in the distance you spot a tiny island, home to a single palm
        tree, just creeping on the horizon. You change course to investigate.
        As you pull up aside, you jump into the clear water, swimming onto the speck of
        land. Propped up against the tree is a skeleton. sun-bleached and picked clean,
        its white bones sit aside a dulled sword and a small book. You pick up the book,
        a few large gold coins falling from between the pages. "The Wolf Queen, v1". You
        open to the first page, but drop it as you feel a shocking sensation run through
        your body. Your hands feel more nimble all of a sudden.
        """
        print(a)
    elif check == 4:
        a = """
        You notice the water turns a shade of green as you pass over what must be a kelp
        field. looking deeper into the murky water, you spot something glimmering in the
        harsh light of the midday sun, entwined in a cluster of kelp leaves, not so far
        from the surface of the water. Taking a deep breath, you dive in, knife in hand
        and cut away the foliage from the wrapped, gilded box. you haul it back onto your
        ship, a suspicious noise coming from inside. the lock is intricately designed
        and without a key, and a regular noise is emenating from within. Almost like a
        beating drum. You store it, and continue.
        """
        print(a)
    elif check == 5:
        a = """
        The crack of cannon-fire alerts you from behind. As you turn to observe you see
        two grand galleons exchanging shots with one another several leagues away from
        your vessel. Still the sound reverberates through the empty air, carried by the
        ocean wind. despite the distance, you still see the tiny figures that are the
        crewmates swinging from each ship to the other in a competiion to defeat the other.
        You decide to speed up and get away from the confrontation, the ocean is a
        dangerous place for anyone to sail alone.
        """
        print(a)
    


main()
