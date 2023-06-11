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
def main():
    #An array of words, second word will be looked through PyDictionary
    opposites_list = [ ["humble", "proud"],
                 ["efficient", "ineffective"],
                 ["smart", "stupid"],
                 ["beautiful", "hideous"],
                 ["scrumptious", "inedible"],
                 ["frugal", "extravagant"],
                 ["ridiculous", "sensible"],
                 ["furious", "calm"] ]

    total_words = len(opposites_list)
    number_of_plays = 10
    print(total_words)

"""
Function to scramble words, passing word argument. 
"""
def jumble_word(word_arg):
    jumbled_char = list(word_arg)  #convert string to List of char (char array)

    for z in range(len(word_arg)):
        RandNum = random.randint(0, (len(word_arg) - 1))
        temp1 = jumbled_char[RandNum]
        temp2 = jumbled_char[RandNum-1]
        jumbled_char[RandNum-1] = temp1
        jumbled_char[RandNum] = temp2

    jumbled_word = ''.join(jumbled_char)
    return jumbled_word

main()
print(jumble_word("armageddon"))
