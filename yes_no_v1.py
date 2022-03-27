# Function that asks the user if they have played the game before
# The function loops until an answer of yes or no has been given
def show_instructions():
    looping_ = True
    while looping_:
        response = input("Have you played this game before? : ")
        if response == "Yes":
            # Temporary text to make it easier to test and check inputs
            print("Regular player")
            return
        elif response == "No":
            print("Instuctions here")
            return
        else:
            print('Please enter either “Yes” or “No”')


# Main routine
show_instructions()
