import random

event_map = [
    [0, 1, 0, 0, 2, 0, 0, 0, 7, 4],
    [0, 0, 3, 0, 0, 0, 3, 0, 3, 1],
    [2, 0, 0, 1, 0, 0, 0, 0, 1, 1],
    [0, 0, 3, 0, 0, 1, 2, 0, 0, 0],
    [6, 0, 0, 0, 1, 0, 0, 0, 0, 2],
    [0, 0, 0, 0, 0, 0, 0, 2, 0, 3],
    [0, 2, 2, 1, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 3, 1, 0, 0],
    [0, 0, 0, 0, 2, 0, 0, 0, 3, 0],
    [1, 0, 5, 0, 0, 2, 0, 2, 0, 1],
]
hintlist = ["\nMaybe gathering some pirate's loot would give you somewhere to start...\n",
            "\nCould that 'NE' be a direction...?\n",
            "\nThe Jolly Roger? That's the symbol of a pirate...\n",
            "\nThe island has to be somewhere on the southern edge of mapped ocean...\n",
            "\nTortuga... If your sense of direction serves you right, it's a few leagues south of the island you washed up on.\n",
            "\nThe harbour town your friend spoke of was west of where you found the pot...\n",
            "\nMaybe the ghost of Hack Narrow can be found somewhere on these seas...\n"]
# Print out grid below in grid pattern, row by row
#for row in event_map:
#    for column in row:
#        print(column, end = " ")
#    print()

'''
event checker takes the parameteres of the player's current position
as well as the event_map list to check if an event needs to be triggered
during the main() function. If so, it checks what function that is and
then calls that function
'''

# The following functions are commented out as they hvae been copied into main.py
# They do not function correctly if they are here, but it's useful to keep them
# here in my opinion as they are all related to event_map

#def fight_event():
#    check = random.randint(1, 3)
#    if check == 1:
#        encounter("easy")
#    elif check == 2:
#        encounter("medium")
#    else:
#        encounter("hard")

#def riddle_event():
#    riddle()

# Maybe add some actual affects of the environmental events? like loss of item, etc.
#def environment_event():
#    global ourHero
#    check = random.randint(1, 6)
#    if check == 1 and done1 == False:
#        a = """
#        A fin breaks the surface of the water infront of you,
#        rising higher and higher out of the water the creature's immense
#        size becomes quickly apparent as the jaws of a huge shark emerges
#        opening wide, revealing row after row of sharp, jagged teeth.
#        Just as it is about to reach your ship, it is dragged underneath.
#        blood rises to sit on the surface of the water and a booming noise
#        comes from below, deafening you completely. Whatever that is, you
#        don't want to run into it. You use a large amount of energy to
#        escape the area as rapidly as possible.
#        """
#        print(a)
#        ourHero.health -= 5
#        print("\n\nDue to the strain of the experience, you lose 5 health")
#        done1 = True
#    elif check == 2 and done2 == False:
#        a = """
#        Sharp scraping from underneath the deck wakes you from a daydream.
#        you see the approaching water is somewhat darker then usual in spots.
#        As you move over another dark spot you see it is a sharp crag of rock
#        underneath the boat... you are moving into shallows.. in the middle of
#        the ocean. You scramble to change course as each second here risks
#        total destruction of the boat. Narrowly you escape from the field with
#        nothing more than a small amount of damage on the underside of your ship.
#        """
#        print(a)
#        ourHero.inventory["Health Potions"] -= 1
#        print("\n\nOne of your health potions gets lost overboard")
#        done2 = True
#    elif check == 3 and done3 == False:
#        a = """
#        Not too far in the distance you spot a tiny island, home to a single palm
#        tree, just creeping on the horizon. You change course to investigate.
#        As you pull up aside, you jump into the clear water, swimming onto the speck of
#        land. Propped up against the tree is a skeleton. sun-bleached and picked clean,
#        its white bones sit aside a dulled sword and a small book. You pick up the book,
#        a few large gold coins falling from between the pages. "The Wolf Queen, v1". You
#        open to the first page, but drop it as you feel a shocking sensation run through
#        your body. Your hands feel more nimble all of a sudden. You pick up the sword
#        and leave the island.
#        """
#        print(a)
#        print("\n\nThe Rusted Sword is added to your inventory")
#        newWeapon = Weapon("Rusted Sword", 8)
#        ourHero.weapons.append(newWeapon)
#        print("\nYou also gain 10 health")
#        if ourHero.health > 90:
#            ourHero.health = 100
#        else:
#            ourHero.health += 10
#        done3 = True
#    elif check == 4 and done4 == False:
#        a = """
#        You notice the water turns a shade of green as you pass over what must be a kelp
#        field. looking deeper into the murky water, you spot something glimmering in the
#        harsh light of the midday sun, entwined in a cluster of kelp leaves, not so far
#        from the surface of the water. Taking a deep breath, you dive in, knife in hand
#        and cut away the foliage from the wrapped, gilded box. you haul it back onto your
#        ship, a suspicious noise coming from inside. the lock is intricately designed
#        and without a key, and a regular noise is emenating from within. Almost like a
#        beating drum. You store it, and continue.
#        """
#        print(a)
#        done4 = True
#    elif check == 5 and done5 == False:
#        a = """
#        The crack of cannon-fire alerts you from behind. As you turn to observe you see
#        two grand galleons exchanging shots with one another several leagues away from
#        your vessel. Still the sound reverberates through the empty air, carried by the
#        ocean wind. despite the distance, you still see the tiny figures that are the
#        crewmates swinging from each ship to the other in a competiion to defeat the other.
#        You decide to speed up and get away from the confrontation, the ocean is a
#        dangerous place for anyone to sail alone.
#        """
#        print(a)
#        done5 = True
#    elif check == 6 and done6 == False:
#        a = """
#        As you pass a series of rocks speared through the waves, you hear a strange but 
#        enticing series of notes hit your ears. Almost instantly and without thought,
#        you turn your head towards the rocks, eager to hear more of the same noise.
#        Even though your skin crawls it urges you towards the rocks, your hands changing the
#        rudder's direction without a conscious thought. The singing becomes stronger, dulling
#        your senses as you move forward in a euphoric but dazed state towards the wet grey rocks.
#        A large wave rocks you off your feet and you hit your head, the trance broken.
#        You recall the old sailor's stories you were told as a child and quickly get the ship
#        back on course, stuffing some spare cloth into your ears. A last glance back and you
#        spot a female figure on the rock. Dead stare and motionless she smiles, revealing
#        a mouthful of needle teeth.
#        """
#        print(a)
#        done6 = True
    

# REPLACE ALL INSTANCES OF CURRENT_POSITION WITH THE APROPRIATE VARIABLE
# FOR WHERE THE PLAYER IS AT EACH ITERATION OF MAIN
#def event_checker(current_position, event_map):
#    if event_map[current_position[1]][current_position[0]] == 1:
#        fight_event()
#    elif event_map(current_position) == 2:
#        riddle()
#    elif event_map(current_position) == 3:
#        environment_event()
                
