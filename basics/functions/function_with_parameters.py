def run():

    # Define function 'climb_ladder' with two parameters (in brackets)
    def climb_ladder(steps_remaining, steps_crossed):

        # Function decisions
        if steps_remaining > steps_crossed:
            print("Still some way to go!")
        elif steps_crossed > steps_remaining:
            print("We are almost there!")

    # Function calls with parameters
    climb_ladder(5,2)
    climb_ladder(2,5)

# call the function when the module is executed directly
if __name__ == "__main__":
    run()