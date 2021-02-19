# Greet user and request character input
print("Program started!")
print("Please enter a standard character: ", end="")
character = input()  # Collect character variable

if len(character) == 1:  # Check length of input (1 character only)
    unicode = ord(character)  # Finds unicode value of character
    print(f"The ASCII code for {character} is {unicode}.")   # Prints response to user
else:
    print("Please enter one character only")  # Error response

print("Program ended!")
