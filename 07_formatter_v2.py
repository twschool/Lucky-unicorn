"""Component 5 - Statement formatter v2
Change v1 into a function
"""


# Function to format text output
def formatter(symbol, text):
    sides = f"{symbol}" * 3
    formatted_text_ = f"{sides} {text} {sides}"
    top_bottom = f"{symbol}" * len(formatted_text_)
    return f"{top_bottom}\n{formatted_text_}\n{top_bottom}"


# Main routine
sides = "*" * 3
text1 = input("Enter the statement you want to format: ")
symbol1 = input("What symbol1 do you want to use: ")
print(formatter(symbol1, text1))
