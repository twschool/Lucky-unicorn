"""LU base component
Components added after they have been created and tested"""

import random


# The function loops until an answer of yes or no has been given
# Yes/no checking function
def yes_no_func(response):
    # If they say yes then skip and output "Program continues"
    if response == "Y" or response == "YES":
        print(f"You entered {response.title()}")
        # Returns False so the loop breaks as a non-invalid answer was entered
        return [False, "Yes"]
    # If they say no, output "Display instructions"
    elif response == "N" or response == "NO":
        print("Display instructions")
        print(f"You entered {response.title()}")
        return [False, "No"]
    else:
        # code triggered when an invalid answer is entered
        print('Please enter either “Yes” or “No”')
        print(f"You entered {response.title()}")
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
    print("**** How to play ****")
    print()
    print("The rules of the game will go here")
    print()


def token_generator(money):
    loop = True
    while loop is True:
        if money <= 0:
            return True
        # Random list of tokens that the random function chooses from
        token = ["Horse", "Donkey", "Unicorn", "Zebra", "Zebra", "Donkey", "Horse", "Zebra", "Donkey", "Horse"]
        # token_choice is the variable that the random token choice is stored inside
        token_choice = random.choice(token)
        # if the token is a unicorn then 4$ is added to the users balance
        if token_choice == "Unicorn":
            money = money + 4
        # if the token is a horse or a donkey 50c is added to the users balance
        elif token_choice == "Horse" or token_choice == "Donkey":
            money = money - 0.5
        # if the token is not either above then the token must be a zebra
        # if the token is a zebra 1$ is taken away from the user
        else:
            money = money - 1
        if money <= 0:
            # if the user runs out of money then the function will return the bool value
            # True as it is True that the user ran out of money
            return True
        quitting = input(f"You have ${money:.2f} left would you\n"
                         f"like to continue (Y)es or (N)o").upper()
        if quitting == "N" or quitting == "NO":
            print(f"You finished with ${money:.2f}")
            # if the user decides to optionally quit with the money they currently have
            # the function will return the value false as it is False that the user ran out of money
            return False
        elif quitting == "Y" or quitting == "YES":
            print("Continuing")


# Main routine
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
    exit("Sorry, you ran out of money")
elif force_quit is False:
    exit("Exited Session")
