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
def get_opposite_word_lists():
    #An array of words, second word will be looked through PyDictionary
    opposites_list = [ ["humble", "proud"],
                 ["efficient", "ineffective"],
                 ["smart", "stupid"],
                 ["beautiful", "hideous"],
                 ["scrumptious", "inedible"],
                 ["frugal", "extravagant"],
                 ["ridiculous", "sensible"],
                 ["furious", "calm"] ]

    return opposites_list

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

def main():

    word_list = get_opposite_word_lists()
    orig_word = word_list[0][0]
    jumbled_word = jumble_word(orig_word)
    opposite_word = word_list[0][1]
    print(orig_word + " = " + jumbled_word + "not " + opposite_word)
    # print(jumble_word("armageddon"))
    # print(generate_random_word_idx(10))


main()

