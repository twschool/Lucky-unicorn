"""Component 4 - game mechanics and looping v2
Based on 06_rounds_v1
removed hard-wiring so that all tokens can be allocated
(random choice 1/16 chance to be a unicorn)
Gives user feedback about number of rounds and
maintains balance
"""

import random
import time
# Added minor time delays to script as sometimes exit print statements would show before earlier print statements
# (used in line 49 and line 52)


def token_generator(money):
    start_balance = money
    loop = True
    rounds_played = 0
    while loop is True:

        rounds_played += 1  # keeps track of rounds
        if money <= 0:
            return True
        # A list containing the available tokens (rigged to be only donkey)
        token = ["Horse", "Horse", "Horse", "Horse", "Horse",
                 "Donkey", "Donkey", "Donkey", "Donkey", "Donkey"
                 , "Zebra", "Zebra", "Zebra", "Zebra", "Zebra"
                 , "Unicorn"]
        token_choice = random.choice(token)
        if token_choice == "Unicorn":
            money += 5
        elif token_choice == "Horse" or token_choice == "Zebra":
            money -= 0.5
        else:
            money -= 1
        if money <= 0:
            print(f"Round {rounds_played}. Token: {token_choice}, Balance: ${money}")
            print("Sorry but you have run out of money\n")
            print(f"You started with ${start_balance:.2f}\nand leave with ${money:.2f}\nThanks for playing")
            return True
        print(f"Round {rounds_played}. Token: {token_choice}, Balance: ${money}")
        quitting = input(f"Would you like to play another round?\n"
                         f"<enter> to play again or 'X' to exit ").upper()
        if quitting == "X" or quitting == "EXIT":
            print(f"You started with {start_balance:.2f}\nand leave with ${money:.2f}\nThanks for playing")
            return False
        else:
            print()


# Main routine
# Temporary money prompt added as the main money prompt is in the base component
# This money prompt crashes if you put in a wrong value like e and doesn't stop you if you put
# In 0 or more than 10$ this will be fixed when the component is moved to the base component
money_ = int(input("Temporary money question prompt\nHow much money do you want to put in: "))
force_quit = token_generator(money_)
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
