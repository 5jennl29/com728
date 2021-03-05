def directions():   # Defines 'directions' function
    direction_list = ["Move forward", "Move backward", "Turn left", "Turn right"]   # Added a list of strings
    return direction_list    # Returns the list


def run():
    directions()    # Calls function 'directions'
    print(directions())   # Prints the result of the function 'directions'


if __name__ == "__main__":  # Runs the function 'run' when file is executed directly
    run()