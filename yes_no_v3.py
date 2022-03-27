"""LU Yes / No
Simplifies the input by converting it to lower case. Also accepts
y or n as abbreviations. Prints result of user choice as well as input - For testing
"""


# Function that asks the user if they have played the game before
# The function loops until an answer of yes or no has been given
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


# Main routine
looping = [True, ""]
response_ = ""
while looping[0] is not False:
    response_ = input("Have you played this game before? : ").upper()
    looping = yes_no_func(response_)
if looping[1] == "No":
    looping[0] = True
    while looping[0] is not False:
        response_ = input("Are you having fun? : ").upper()
        looping = yes_no_func(response_)
    if looping[1] == "No":
        print("That's bad")
    else:
        print("Good")
elif looping[1] == "Yes":
    print("We have a regular")
