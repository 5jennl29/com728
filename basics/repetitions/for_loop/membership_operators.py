print()
print("What phrase do you see?") # Ask user for input (phrase)
phrase = input()

print()
print("Reversing...")
print("The phrase is: ", end="")

reversed = ""  # Reversed is the phrase string

for letter in phrase:  # Taking each letter in the phrase...
    reversed = letter + reversed   # And adding the next one in front of it, thereby reversing the order.

print(reversed)