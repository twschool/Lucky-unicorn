"""Component 2 (How much) v1
Ask user how much they want to play with and check that the
input is a valid integer between 1 and 10. If it is this amount becomes the balance in
their accounts"""


def number_checker():
    low = 1
    high = 10
    error = "Please enter a whole number between 1 and 10\n"
    user_balance = 0
    while not low <= user_balance <= high:
        try:
            user_balance = int(input("How much money do you want to play"
                                     " with\n(must be a whole number between 1 and 10) $: "))
        except ValueError:
            user_balance = 0
            print(error)
    print(f"You are playing with {user_balance}$")

user_balance_ = number_checker()
