"""Component 5 - Statement formatter v3
Call function 3 times - once for each of the tests
"""


# Function to format text output
def formatter(symbol, text):
    sides = f"{symbol}" * 3
    formatted_text_ = f"{sides} {text} {sides}"
    top_bottom = f"{symbol}" * len(formatted_text_)
    return f"{top_bottom}\n{formatted_text_}\n{top_bottom}"


# Main routine
print(formatter("-", "Welcome to the Lucky Unicorn Game"))
print()
print(formatter("!", "Congratulations, you got a unicorn"))
print()
print(formatter("*", "Goodbye"))
