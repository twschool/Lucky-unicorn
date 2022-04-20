"""LU final version based on LU-base_v3
Final version of project
"""

import random
import time


# The function loops until an answer of yes or no has been given
# Yes/no checking function


def yes_no_func(response):
    # If they say yes then skip and output "Program continues"
    if response == "Y" or response == "YES":
        # Returns False so the loop breaks as a non-invalid answer was entered
        return [False, "Yes"]
    # If they say no, output "Display instructions"
    elif response == "N" or response == "NO":
        return [False, "No"]
    else:
        # code triggered when an invalid answer is entered
        print('Please enter either “Yes” or “No”')
        # Returns True as a Valid answer was entered
        return [True, ""]


# Number checking function
def number_checker(question, low, high):
    error = "Please enter a whole number between 1 and 10\n"
    # Keep asking until a valid amount (1-10) is entered
    while True:
        try:
            response = int(input(question))
            if low <= response <= high:
                return response
            else:
                print(error)
        except ValueError:
            print(error)


# Function to display instructions
def show_instructions():
    print(formatter("*", "How to play"))
    print()
    print("Choose a starting amount to play with - must be between $1 and $10")
    print()
    print("Then pressed <enter> to play. You will get a random token which might "
          "be a horse, a\nzebra, a donkey, or a unicorn")
    print()
    print("It costs $1 to play each round but, depending on your prize, you "
          "could win some of your\nmoney back. These are the payout amounts:\n"
          "\tUnicorn: $5 (balance increases by $4\n"
          "\tHorse: $0.50 (balance decreases by $0.50\n"
          "\tZebra: $0.50 (balance decreases by $0.50\n"
          "\tDonkey: 0.00 (balance decreases by $1\n")
    print("\nSee if you can avoid donkeys, get the unicorns, and finish with"
          "\nmore money than you started with.")
    print("*" * 65)
    print()


# Function to generate random token
def token_generator(money):
    loop = True
    starting_money = money
    while loop is True:
        if money <= 0:
            return True
        global round_number
        round_number += 1
        print(formatter(".", f"Round {round_number}"))
        print()
        # Random list off tokens that the random function chooses from
        # I wrote my own code for this so that is why it's not a random number from 0-100 choosing
        token = ["Horse", "Horse", "Horse", "Horse", "Horse",
                 "Donkey", "Donkey", "Donkey", "Donkey", "Donkey",
                 "Zebra", "Zebra", "Zebra", "Zebra", "Zebra",
                 "Unicorn"]
        # token_choice is the variable that the random token choice is stored inside
        token_choice = random.choice(token)
        # if the token is a unicorn then 4$ is added to the users balance
        if token_choice == "Unicorn":
            money = money + 4
            print(formatter("!", f"Congratulations, you got a unicorn, Your balance is now ${money:.2f}"))
            print()
        # if the token is a horse or a donkey 50c is added to the users balance
        elif token_choice == "Horse":
            money -= 0.5
            print(formatter("H", f"You got a horse, Your balance is now ${money:.2f}"))
            print()
        elif token_choice == "Zebra":
            money -= 0.5
            print(formatter("Z", f"You got a Zebra, Your balance is now ${money:.2f}"))
            print()
        # if the token is not either above then the token must be a donkey
        # if the token is a zebra 1$ is taken away from the user
        else:
            money = money - 1
            print(formatter("D", f"Bad luck, you got a donkey, Your balance is now ${money:.2f}"))
            print()
        if money <= 0:
            # if the user runs out of money then the function will return the bool value
            # True as it is True that the user ran out of money
            print(f"Sorry but you have ran out of money\n")
            print(formatter("=", "Thanks for playing"))
            print(f"\nYou started with ${starting_money:.2f}\nand leave with ${money:.2f}")
            return True
        quitting = input(f"<enter> to continue or X to exit: ").upper()
        if quitting == "X":
            print(formatter("=", "Thanks for playing"))
            print(f"You started with ${starting_money:.2f}\nand leave with ${money:.2f}")
            # if the user decides to optionally quit with the money they currently have
            # the function will return the value false as it is False that the user ran out of money
            return False
        else:
            print("Continuing")


# Function to format text output
def formatter(symbol, text):
    sides = f"{symbol}" * 3
    formatted_text_ = f"{sides} {text} {sides}"
    top_bottom = f"{symbol}" * len(formatted_text_)
    return f"{top_bottom}\n{formatted_text_}\n{top_bottom}"


# Main routine
round_number = 0
print(formatter("-", "Welcome to the Lucky Unicorn Game"))
print()
looping = [True, ""]
response_ = ""
played_before = ""
while looping[0] is not False:
    response_ = input("Have you played this game before? : ").upper()
    # This code runs the answer through a function to determine if the answer is a
    # Valid answer (Either 'yes' or 'no')
    looping = yes_no_func(response_)
    played_before = looping[1]
if played_before == "No":
    # If the user has not played before then this code will call the function
    # That prints the instructions
    show_instructions()
user_balance_ = number_checker("How much would you like to play with? $", 1, 10)
# Tells the user how much money they are playing with based on the input they put in
print(f"You are playing with ${user_balance_}")
# Force quit is a variable that is set to True when the user runs out of money and set to False
# when the user decides to optionally quit the game with the amount of money they currently have
force_quit = token_generator(user_balance_)
if force_quit is True:
    # Code which ends the program when the user runs out of money
    print()
    print(formatter("*", "Goodbye"))
    time.sleep(0.1)
elif force_quit is False:
    print()
    print(formatter("*", "Goodbye"))
    time.sleep(0.1)
    exit("Exited Session")
