import random

event_map = [
    [0, 1, 0, 0, 2, 0, 0, 0, 0, 0],
    [0, 0, 3, 0, 0, 0, 3, 0, 3, 1],
    [2, 0, 0, 1, 0, 0, 0, 0, 1, 1],
    [0, 0, 3, 0, 0, 1, 2, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 2],
    [0, 0, 0, 0, 0, 0, 0, 2, 0, 3],
    [0, 2, 2, 1, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 3, 1, 0, 0],
    [0, 0, 0, 0, 2, 0, 0, 0, 3, 0],
    [1, 0, 0, 0, 0, 2, 0, 2, 0, 1],
]
# Print out grid below in grid pattern, row by row
for row in event_map:
    for column in row:
        print(column, end = " ")
    print()

'''
event checker takes the parameteres of the player's current position
as well as the event_map list to check if an event needs to be triggered
during the main() function. If so, it checks what function that is and
then calls that function
'''

def fight_event():
    check = random.randint(1, 3)
    if check == 1:
        encounter("easy")
    elif check == 2:
        encounter("medium")
    else:
        encounter("hard")

def riddle_event():
    riddle()

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
    

# REPLACE ALL INSTANCES OF CURRENT_POSITION WITH THE APROPRIATE VARIABLE
# FOR WHERE THE PLAYER IS AT EACH ITERATION OF MAIN
def event_checker(current_position, event_map):
    if event_map(current_position) == 1:
        fight_event()
    elif event_map(current_position) == 2:
        riddle()
    elif event_map(current_position) == 3:
        environment_event()
                
