print()
print("How many numbers should I sum up?") #request for user input (numbers to add)
numbers_to_add = int(input())

added = 1 #added starts at 1 (first number to add)

total = 0 #running total

while added <= numbers_to_add:
    print(f"Please enter number {added} of {numbers_to_add}:")
    number = int(input())   # user input of next number to add
    total = total + number   # running total incl user input
    added = added + 1

print(f"The total is {total}.")