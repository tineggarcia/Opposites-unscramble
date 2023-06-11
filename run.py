"""
A simple game to test your vocabulary skills
by unscrambling the hidden antonym word
"""
import random

from PyDictionary import PyDictionary
dictionary=PyDictionary()

"""
main function, holds the dictionary
"""

def _init():
    #An array of words, second word will be looked through PyDictionary
    WORDLIST = [ ["humble", "proud", get_word_meaning("proud")],
                 ["efficient", "ineffective", get_word_meaning("ineffective")],
                 ["smart", "stupid", get_word_meaning("stupid")],
                 # ["beautiful", "hideous", get_word_meaning("hideous")],
                 # ["scrumptious", "inedible", get_word_meaning("inedible")],
                 # ["frugal", "extravagant", get_word_meaning("extravagant")],
                 # ["ridiculous", "sensible", get_word_meaning("sensible")],
                 # ["furious", "calm", get_word_meaning("calm")],
                 # ["generous", "selfish", get_word_meaning("selfish")],
                 # ["joyful", "sad", get_word_meaning("sad")],
                 # ["compassionate", "heartless", get_word_meaning("heartless")],
                 # ["exaggerated", "understated", get_word_meaning("understated")],
                 # ["drab", "cheerful", get_word_meaning("cheerful")],
                 # ["filthy", "clean", get_word_meaning("clean")],
                 # ["peculiar", "normal", get_word_meaning("normal")],
                 # ["prudent", "unwise", get_word_meaning("unwise")],
                 # ["flamboyant", "modest", get_word_meaning("modest")],
                 # ["infantile", "mature", get_word_meaning("mature")],
                 # ["fallacious", "true", get_word_meaning("true")],
                 # ["pristine", "dirty", get_word_meaning("dirty")],
                 # ["deafening", "soft", get_word_meaning("soft")],
                 # ["swift", "slow", get_word_meaning("slow")],
                 # ["plausible", "unlikely", get_word_meaning("unlikely")],
                 ["rigid", "flexible", get_word_meaning("flexible")]

                 ]

    return WORDLIST

"""
Function to scramble words, passing word argument. 
"""
def jumble_word(word_arg):
    jumbled_char = list(word_arg)

    for z in range(len(word_arg)):
        rand_num = random.randint(0, (len(word_arg) - 1))
        temp1 = jumbled_char[rand_num]
        temp2 = jumbled_char[rand_num-1]
        jumbled_char[rand_num-1] = temp1
        jumbled_char[rand_num] = temp2

    jumbled_word = ''.join(jumbled_char)
    return jumbled_word

#Generate array of random numbers without DUPLICATES
def generate_random_word_idx(no_of_words):
    random_idx = []
    for w in range(0,no_of_words):
        random_idx.append(-1)

    counter = 0

    while(counter < no_of_words):
        random_num = random.randint(0, (no_of_words - 1))
        if not random_num in random_idx:
            random_idx[counter] = random_num
            counter += 1
    return random_idx

def get_word_meaning(word):
    # default to word if no meaning from PyDictionary
    word_meaning = word
    meanings = dictionary.meaning(word)
    if meanings != None:
        word_meaning = list(meanings.values())[0][0]
    return word_meaning

def main():

    word_list = _init()
    for word in word_list:
        print(word)

    orig_word = word_list[3][0]
    jumbled_word = jumble_word(orig_word)
    opposite_word = word_list[3][1]
    opposite_def = get_word_meaning(opposite_word)
    print(orig_word + " is " + jumbled_word + " not " + opposite_word)
    print(opposite_def)



main()

