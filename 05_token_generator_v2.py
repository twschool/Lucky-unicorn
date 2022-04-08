"""Component 3 (random token) v2
Generates random choice of token in random order
the amount of times the user wants to run
the program"""
import random


def token_generator(money):
    loop = True
    while loop is True:
        if money <= 0:
            return True
        token = ["Horse", "Donkey", "Unicorn", "Zebra", "Zebra", "Donkey", "Horse", "Zebra", "Donkey", "Horse"]
        token_choice = random.choice(token)
        if token_choice == "Unicorn":
            money = money + 4
        elif token_choice == "Horse" or token_choice == "Zebra":
            money = money - 0.5
        else:
            money = money - 1
        if money <= 0:
            return True
        quitting = input(f"You have ${money} left would you\n"
                         f"like to continue (Y)es or (N)o").upper()
        if quitting == "N" or quitting == "NO":
            print(f"You finished with ${money}")
            return False
        elif quitting == "Y" or quitting == "YES":
            print("Continuing")


# Main routine
# Temporary money prompt added as the main money prompt is in the base component
# This money prompt crashes if you put in a wrong value like e and doesn't stop you if you put
# In 0 or more than 10$ this will be fixed when the component is moved to the base component
money_ = int(input("Temporary money question prompt\nHow much money do you want to put in: "))
force_quit = token_generator(money_)
if force_quit is True:
    exit("Exited Session")
elif force_quit is False:
    exit("Exited Session")
