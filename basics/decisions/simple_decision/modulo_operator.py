def run():
    # Ask user to enter a whole number
    print("Please enter a whole number.")
    # Store number as variable named number
    number = int(input())

    # Display message 'odd' or 'even'.
    if number % 2 == 0:
        print(f"The number {number} is an even number.")
    else:
        print(f"The number {number} is an odd number.")

# call the function when the module is executed directly
if __name__ == "__main__":
    run()
