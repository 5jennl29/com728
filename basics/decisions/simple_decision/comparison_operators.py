def run():

    # Ask user for first number
    print("Please enter the first number...")
    first_number = int(input())

    # Ask user for second number
    print("Please enter the second number...")
    second_number = int(input())

    # Decisions
    if first_number < second_number:
        print("The first number is smallest!")

    elif second_number < first_number:
        print("The second number is smallest!")

    else:
        print("Both numbers are equal!")

# call the function when the module is executed directly
if __name__ == "__main__":
    run()