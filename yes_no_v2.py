"""LU Yes / No
Simplifies the input by converting it to lower case. Also accepts
y or n as abbreviations. Prints result of user choice as well as input - For testing
"""


# Function that asks the user if they have played the game before
# The function loops until an answer of yes or no has been given
def show_instructions():
    looping_ = True
    while looping_:
        response = input("Have you played this game before? : ").upper()
        if response == "Y" or response == "YES":
            # Temporary text to make it easier to test and check inputs
            print("Program continues")
            print(f"You entered {response}")
            return
        elif response == "N" or response == "NO":
            print("Display instructions")
            print(f"You entered {response}")
            return
        else:
            print('Please enter either “Yes” or “No”')
            print(f"You entered {response}")


# Main routine
show_instructions()
