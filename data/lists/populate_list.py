def directions():                                                                 # Defines 'directions' function
    directions = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]     # Stores a list called 'directions'
    return directions                                                             # Returns the list


def menu():                                         # Defines 'menu' function
    print("Please select a direction:")
    dirs = directions()                             # Variable 'dirs' stores the returned list

    for index in range(len(dirs)):                  # For each indexed item in the range of the whole list (len) 'dirs'
        print(f"{index} : {dirs[index]}")           # Print the item {index} : and the {item within that index location}

    response = int(input())                     # Reads in user response (integer)
    return dirs[response]


def run():                                      # Def 'run' function
    route = []                                  # Stores variable 'route' as an empty list
    print("Working out escape route...\n")
    for _ in range(5):                          # For _ 'blank' in range (5) - for 5 times
        escape_route = menu()                   # Creates a variable called 'escape_route' to store user responses from the call of the 'menu' function
        route.append(escape_route)              # Appends (adds) those responses to the list 'route'

    print(f"Escape route: {route}.")            # Prints out the user-defined route out of the maze


if __name__ == "__main__":                      # Runs the function 'run' when file is executed directly
    run()