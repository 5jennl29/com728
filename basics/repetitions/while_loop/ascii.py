def run():

    # Ask user for number of bars to be charged
    print("How many bars should be charged?")
    num_bars = int(input())

    # Declare a control variable
    charging_bars = 0

    print()

    # live cables loop
    while charging_bars < num_bars:
        print("Charging:", end="")        # end="empty string" will keep next print statement on the same line.
        charging_bars = charging_bars + 1       # this is adding +1 on each loop
        print((charging_bars * " █"))       # this is using the counter 'charging_bars' to apply to the shape █

    print()
    print("The battery is fully charged.")

# call the function when the module is executed directly
if __name__ == "__main__":
    run()