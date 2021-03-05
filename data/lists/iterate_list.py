def directions():                                                         # Defines 'directions' function
    directions = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]     # Stores a list
    return directions                                                            # Returns the list


def menu():                                              # Defines 'menu' function
    print("Please select a direction:")
    dirs = directions()                             # Variable 'dirs' stores the returned list

    for index in range(len(dirs)):                  # For each indexed item in the range of the whole list (len) 'dirs'
        print(f"{index} : {dirs[index]}")           # Print the item {index} : and the {item within that index location}


def run():
    menu()                                   # Calls 'menu' function


if __name__ == "__main__":  # Runs the function 'run' when file is executed directly
    run()