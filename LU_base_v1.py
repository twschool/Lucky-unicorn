"""LU base component
Components added after they have been created and tested"""


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
user_balance_ = number_checker("How much would you like to play with? $", 1, 10)
print(f"You are playing with ${user_balance_}")
