"""Component 3 (random token) v1
Generates random choice of token in random order 100
times to fine tune the percentage chance
of winning so the house wins most of the time"""
import random


def token_generator():
    money = 100
    for num in range(0, 100):
        token = ["Horse", "Horse", "Horse", "Horse", "Horse",
                 "Donkey", "Donkey", "Donkey", "Donkey", "Donkey",
                 "Zebra", "Zebra", "Zebra", "Zebra", "Zebra",
                 "Unicorn"]
        token_choice = random.choice(token)
        if token_choice == "Unicorn":
            money = money + 4
        elif token_choice == "Horse" or token_choice == "Zebra":
            money = money - 0.5
        else:
            money = money - 1
        print(f"Token: {token_choice}\n${money}")
    print(f"Starting balance $100\n"
          f" Final balance ${money}")



# Main routine
token_generator()
