def run():
    # Define first function
    def display_ladder(steps):
        print("\n| |")  # prints ladder top
        for step in range(steps):  # prints rest of ladder per no. of 'steps'
            print("***")
            print("| |")

    # Define second function (user input)
    def create_ladder():
        print("How many steps remain?")
        steps = int(input())  # Input here (number of steps)
        display_ladder(steps)  # Calls first function with parameter 'steps'

    # Call second function for user input
    create_ladder()

# call the function when the module is executed directly
if __name__ == "__main__":
    run()