print()
print("How many rows should I have?")
rows = int(input())  # Stores number of rows input by user

print()
print("How many columns should I have?")
columns = int(input()) # Stores number of columns input by user

print()
print("Here I go:")

for count in range(0, rows, 1): # Starts at 0, ends at 'rows' variable, counts up by 1
    for count in range(0, columns, 1):  # Starts at 0, ends at 'columns' variable, counts up by 1
        print(" ;) ", end="")   # Prints the emoji columns all on same line
    print() # Prints the emoji rows on separate lines