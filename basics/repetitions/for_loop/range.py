def run():

    print()
    print("What level of brightness is required?") # Requests user input - value of brightness
    bright = int(input()) # Stores user input


    print("\nAdjusting brightness...\n")


    for bright in range (2, bright + 1, 2):  # For value of 'bright' in range starting at 2, to value 'bright, in steps of 2 (even numbers only)
        print(f"Beep's brightness level: {'*' * bright}")
        print(f"Beep's brightness level: {'*' * bright}")
        print()

    print("Adjustments complete!") # Completion statement

# call the function when the module is executed directly
if __name__ == "__main__":
    run()
