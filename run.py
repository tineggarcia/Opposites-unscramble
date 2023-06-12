"""
A simple game to test your vocabulary skills
by unscrambling the hidden antonym word
"""
import os
import random
import argparse

from PyDictionary import PyDictionary

dev_mode = (os.environ.get("devMode") == "true")

#An array of words, second word(antonym) will be looked through PyDictionary for displayed text
full_word_list = [ ["humble", "proud"],
              ["efficient", "ineffective"],
              ["smart", "stupid"],
              ["beautiful", "unattractive"],
              ["scrumptious", "inedible"],
              ["frugal", "extravagant"],
              ["ridiculous", "sensible"],
              ["furious", "calm"],
              ["generous", "selfish"],
              ["joyful", "sad"],
              ["compassionate", "heartless"],
              ["exaggerated", "understated"],
              ["drab", "cheerful"],
              ["filthy", "clean"],
              ["peculiar", "normal"],
              ["prudent", "unwise"],
              ["flamboyant", "modest"],
              ["infantile", "mature"],
              ["fallacious", "true"],
              ["pristine", "dirty"],
              ["deafening", "soft"],
              ["swift", "slow"],
              ["plausible", "unlikely"],
              ["rigid", "flexible"]
            ]

"""
initialise the words and it's opposite meaning
"""
def init_word_meaning_list(random_idx):
    word_list = []
    antonym_word_list = []
    for x in random_idx:
        antonym_word_list.append(full_word_list[x][1])

    word_dictionary = PyDictionary()
    word_dictionary.__init__(antonym_word_list)

    word_meanings = word_dictionary.getMeanings()

    # not the best loop - Fix it next time
    for items in full_word_list:
        word_meaning = word_meanings.get(items[1])
        if word_meaning != None:
            word_list.append([items[0],items[1], list(word_meaning.values())[0][0]])
    return word_list

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
    total_word_count = len(full_word_list)
    random_idx = [-1] * no_of_words
    counter = 0
    while(counter < no_of_words):
        random_num = random.randint(0, (total_word_count - 1))
        if not random_num in random_idx:
            random_idx[counter] = random_num
            counter += 1
    return random_idx

def validate_no_of_words(value):
    try:
        no_of_words_to_answer = int(value)
        # don't validate when running dev mode
        if dev_mode:
            return True
        if no_of_words_to_answer < 10 or no_of_words_to_answer > 20:
            print(f"Invalid input {value}, please try again.\n")
            return False
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False

    return True

def validate_YN(val):
    if val == 'Y' or val == 'N':
        return True
    else:
        return False

def show_no_of_words_input():
    answer = input("Please enter how many games/words to guess you want to play(between 10 - 20)?  >>> ")

    no_of_words_to_answer = 0
    if validate_no_of_words(answer):
        no_of_words_to_answer = int(answer)
    else:
        no_of_words_to_answer = show_no_of_words_input()

    return no_of_words_to_answer
def main(no_of_words_to_answer):

    random_idx = generate_random_word_idx(no_of_words_to_answer)

    print("\nInitialising word bank, please wait ...\n")
    word_list = init_word_meaning_list(random_idx)

    print("\nGame starts now ...\n")

    points_earned = 0
    for x in range(0,no_of_words_to_answer):
        points_available = 2
        word_to_answer = word_list[x]
        actual_word = word_to_answer[0]
        opposite_word = word_to_answer[1]
        opposite_meaning = word_to_answer[2]
        jumbled_word = jumble_word(actual_word)

        print(f"\nYou got {points_earned} so far. Points available for this question is {points_available}.")
        print(f"Word # {str((x + 1))} clue: What word doesn't mean '{opposite_meaning}'")
        answer = input(f"Re-earrange these jumbled letters: '{jumbled_word}'. >>> ")
        if answer == actual_word:
            points_earned = points_earned + points_available
        else:
            points_available = points_available - 1
            answer = input(f"\nWrong! try again. Points available for this question is {points_available}. "
                           f"\nAnother clue..what's the opposite of {opposite_word}?"
                           f"\nRe-earrange these jumbled letters: '{jumbled_word}'. >>> ")
            if answer == actual_word:
                points_earned = points_earned + points_available
            else:
                points_available = points_available - 1

        if points_available > 0:
            print(f"\nCorrect! You earned {points_available} points.")
            print(f"{actual_word} is not {opposite_word} nor {opposite_meaning}\n\n")
        else:
            print(f"\nSorry, the answer is {actual_word}.\nYou did not earned any points for this question.\n\n")

    perfect_score =  no_of_words_to_answer*2
    if points_earned == no_of_words_to_answer*2:
        print(f"You are one in a million! Wow! Perfect score - {points_earned}/{perfect_score}")
    elif points_earned > no_of_words_to_answer:
        print(f"You got it in you! Your final score is {points_earned}/{perfect_score}.")
    else:
        print(f"Better luck next time. Your final score is {points_earned}/{perfect_score}.")

    show_play_again = True
    while show_play_again:
        play_again = input(f"\n\nDo you want to play again? Y/N >>> ")
        if validate_YN(play_again):
            show_play_again = False
            if play_again == "Y":
                no_of_words_to_answer = show_no_of_words_input()
                main(no_of_words_to_answer)
            else:
                print("Thanks for playing! Goodbye...")


def parse_arguments():
    parser = argparse.ArgumentParser()

    # add command line arg options
    parser.add_argument("no_of_words_to_answer", type=int, nargs='?', help="Provide number of words to answer per session.(Optional)")

    arg = parser.parse_args()

    no_of_words_to_answer = arg.no_of_words_to_answer

    return no_of_words_to_answer


def show_welcome_instructions():
    print("==================================================")
    print("Hello! Welcome to Unscrambling the Opposites Game!")
    print("==================================================\n")
    print("*** Rules of the Game ***\nGuess the jumbled words and unscramble it based on the clues provided.\n")

# start of program here
show_welcome_instructions()

# first check if there is an argument passed during running of script in command line
no_of_words_to_answer = parse_arguments()
if no_of_words_to_answer == None:
    no_of_words_to_answer = show_no_of_words_input()

main(no_of_words_to_answer)

