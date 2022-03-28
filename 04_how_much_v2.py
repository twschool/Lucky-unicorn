"""Component 2 (How much) v2
Ask user how much they want to play with and check that the
input is a valid integer between 1 and 10. If it is this amount becomes the balance in
their accounts"""
# Optimised code with teachers example


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


user_balance_ = number_checker("How much would you like to play with? $", 1, 10)
print(f"You are playing with ${user_balance_}")
