def run():

    print()
    print("How far are we (in steps) from the cave?") # Request for user input
    steps = int(input())

    print()
    for count in range(steps, 0, -1):  # Counting down from number of steps (user input), to zero, one step at a time (-1)
        print(f"{steps} steps remaining.") # Prints how many steps remaining after each step is taken
        steps = steps - 1

    print()
    print("We have reached the cave!")

# call the function when the module is executed directly
if __name__ == "__main__":
    run()