# Ask user to enter a whole number
print("Please enter a whole number.")
# Store number as variable named number
number = int(input())

# Display message 'odd' or 'even'.
if number % 2 == 0:
    print(f"The number {number} is an even number.")
else:
    print(f"The number {number} is an odd number.")
