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
    WORDLIST = [ ["humble", "proud", get_word_meaning("proud", "proud")],
                 ["efficient", "ineffective", get_word_meaning("ineffective", "ineffective")],
                 ["smart", "stupid", get_word_meaning("stupid", "stupid")],
                 ["beautiful", "hideous", get_word_meaning("hideous", "hideous")],
                 ["scrumptious", "inedible", get_word_meaning("inedible", "inedible")],
                 ["frugal", "extravagant", get_word_meaning("extravagant", "extravagant")],
                 ["ridiculous", "sensible", get_word_meaning("sensible", "sensible")],
                 ["furious", "calm", get_word_meaning("calm", "calm")]]

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

def get_word_meaning(word, default_meening):
    word_meaning = default_meening
    meanings = dictionary.meaning(word)
    if meanings != None:
        meaning = list(meanings.values())[0][0]
    return meaning

def main():

    word_list = _init()
    for word in word_list:
        print(word)

    orig_word = word_list[3][0]
    jumbled_word = jumble_word(orig_word)
    opposite_word = word_list[3][1]
    opposite_def = get_word_meaning(opposite_word, opposite_word)
    print(orig_word + " is " + jumbled_word + " not " + opposite_word)
    print(opposite_def)


main()

