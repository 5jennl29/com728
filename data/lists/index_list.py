def movements():   # Defines function called 'movements'
    path = ["Move Forward", 10, "Move Backward", 5, "Move Left", 3, "Move Right", 1]    # Created list called 'path'
    return path   # Return the list 'path'


def run():   # Defines function called 'movements'
    print("\nMoving...")
    direction = movements()       # Created variable called 'direction' with the returned info from function called 'movements'
    print(f"{direction[0]} for {direction[1]} steps.")     # Prints items in the list, called by their index number
    print(f"{direction[2]} for {direction[3]} steps.")
    print(f"{direction[4]} for {direction[5]} steps.")
    print(f"{direction[6]} for {direction[7]} steps.")


if __name__ == "__main__":  # Runs the function 'run' when file is executed directly
    run()