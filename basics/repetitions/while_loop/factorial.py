def run():

    print()
    print("Please enter a number.") #request for user input (number to find factorial of)
    number = int(input())

    total = 1 #running total
    counter = 0 #counter (counting the number of times to run the loop)

    while number > counter:
        counter = counter + 1  #adds to the counter with each loop
        total = total * counter   # running total

    print(f"The factorial is {total}.")

# call the function when the module is executed directly
if __name__ == "__main__":
    run()