"""Component 4 - game mechanics and looping v1
Based on 05_token_generator_v2 but hard-wired to only allocate donkeys
Gives user feedback about number of rounds and maintains balance.
Test amount set to 5$
"""

import random
import time
# Added minor time delays to script as sometimes exit print statements would show before earlier print statements
# (used in line 49 and line 52)


def token_generator():
    loop = True
    ROUND_START = 0
    TEST_AMOUNT = 5
    money = TEST_AMOUNT
    rounds_played = ROUND_START
    while loop is True:
        rounds_played += 1  # keeps track of rounds
        if money <= 0:
            return True
        # A list containing the available tokens (rigged to be only donkey)
        token = ["Donkey", "Donkey", "Donkey"]
        token_choice = random.choice(token)
        if token_choice == "Donkey":
            money = money - 1
        if money <= 0:
            print(f"Round {rounds_played}. Token: {token_choice}, Balance: ${money}")
            print("Sorry but you have run out of money\n")
            print(f"You started with ${TEST_AMOUNT:.2f}\nand leave with ${money:.2f}\nThanks for playing")
            return True
        print(f"Round {rounds_played}. Token: {token_choice}, Balance: ${money}")
        quitting = input(f"Would you like to play another round?\n"
                         f"<enter> to play again or 'X' to exit ").upper()
        if quitting == "X" or quitting == "EXIT":
            print(f"You started with {TEST_AMOUNT:.2f}\nand leave with ${money:.2f}\nThanks for playing")
            return False
        else:
            print()


# Main routine
# Temporary money prompt added as the main money prompt is in the base component
# This money prompt crashes if you put in a wrong value like e and doesn't stop you if you put
# In 0 or more than 10$ this will be fixed when the component is moved to the base component
force_quit = token_generator()
if force_quit is True:
    # Added a minor time delay to script as sometimes the 'exited session' text would print before
    # the 'You ran out of money' text would show
    print("Goodbye")
    time.sleep(0.1)
    exit("Exited Session")
elif force_quit is False:
    print("Goodbye")
    time.sleep(0.1)
    exit("Exited Session")
