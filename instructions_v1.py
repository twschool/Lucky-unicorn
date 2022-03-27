"""Took function from component yes_no checker as the basis for this
new function which incorporates both yes/no and show instructions"""


# The function loops until an answer of yes or no has been given
# Yes/no checking function
def yes_no_func(response):
    # If they say yes then skip and output "Program continues"
    if response == "Y" or response == "YES":
        print("Program continues")
        print(f"You entered {response.title()}")
        # Returns False so the loop breaks as a non-invalid answer was entered
        return [False, "Yes"]
    # If they say no, output "Display instructions"
    elif response == "N" or response == "NO":
        print("Display instructions")
        print(f"You entered {response.title()}")
        return [False, "No"]
    else:
        print('Please enter either “Yes” or “No”')
        print(f"You entered {response.title()}")
        # Returns True as a Valid answer was entered
        return [True, ""]


# Function to display instructions
def show_instructions():
    print("**** How to play ****")
    print()
    print("The rules of the game will go here")
    print()
    print("Program continues")
    print()


# Main routine
looping = [True, ""]
response_ = ""
played_before = ""
while looping[0] is not False:
    response_ = input("Have you played this game before? : ").upper()
    looping = yes_no_func(response_)
    played_before = looping[1]
if played_before == "No":
    show_instructions()
