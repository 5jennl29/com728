# Ask user to enter first whole number
print("Please enter the first whole number.")
# Store number as variable named first_number
first_number = int(input())

# Ask user to enter second whole number
print("Please enter the second whole number.")
# Store number as variable named second_number
second_number = int(input())

# Ask user to enter third whole number
print("Please enter the third whole number.")
# Store number as variable named third_number
third_number = int(input())

# Variables (the counters) for odd and even (a box to put odd or even into!)
even_numbers = 0
odd_numbers = 0

# if first number returns 0 remainder when * 2, add a 1 to the even_numbers variable (the counter)
if first_number % 2 == 0:
    even_numbers = even_numbers + 1
else:
    odd_numbers = odd_numbers + 1

# same decision for second_number
if second_number % 2 == 0:
    even_numbers = even_numbers + 1
else:
    odd_numbers = odd_numbers + 1

# same decision for third_number
if third_number % 2 == 0:
    even_numbers = even_numbers + 1
else:
    odd_numbers = odd_numbers + 1

# shows how many odds and evens were in each counter
print(f"There were {even_numbers} even numbers and {odd_numbers} odd numbers.")