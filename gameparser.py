#gameparser.py
import string
legal_words = ["go", "attack", "take", "drop", "south", "north", "east", "west", "exit", "credits", "start", "check", "inventory", "gear", "weapons","health","heal","fight", "drink", "potion"]
#This is the list of words that the game "understands". Anything else
#is taken out before any commands are processed.

def filter_words(words, legal_words): #This function removes any words not in the list legal_words from a list of words
    filtered_words = []
    for x in words:
        if x.lower() in legal_words:
            filtered_words.append(x)
        else:
            pass
    return filtered_words

def remove_punct(text): #Removes punctuation from a string
    no_punct = ""
    for char in text:
        if not (char in string.punctuation):
            no_punct = no_punct + char
    return no_punct

def remove_spaces(text): #Removes leading and trailing spaces from a string
    new_text = []
    for char in text:
        new_text.append(char)
    while True:
        if len(new_text) > 0:
            if new_text[0] == " ":
                del new_text[0]
            elif new_text[-1] == " ":
                del new_text[-1]
            elif new_text[0] != " " and new_text[-1] != " ":
                break
        else:
            break
    new_text = "".join(new_text)
    return new_text

def normalise_input(user_input): #Combines the above functions to turn any input into something understandable by the game
    no_punct = remove_punct(user_input).lower() #Removes punctuation and makes every letter lowercase
    no_punct_and_whitespace = remove_spaces(no_punct) #Removes leading and trailing spaces
    word_list = no_punct_and_whitespace.split() #Turns the string of words into a list
    word_list = filter_words(word_list, legal_words) #Filters any "illegal" words from the list and returns it
    return word_list

def normalise_answer(user_input): #The same as above but does not filter words, used so answers to riddles are not recognised by the rest of the game
    no_punct = remove_punct(user_input).lower()
    no_punct_and_whitespace = remove_spaces(no_punct)
    word_list = no_punct_and_whitespace.split()
    return word_list
