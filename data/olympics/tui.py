screen_width = 75                                # Variable the determines the width of the screen

def started(msg=""):                                # Calls this function with a message that's set to an empty string
    output = f"Operation started: {msg}"            # Output message to user
    dashes = "-" * screen_width                     # Sets dashes to the length specified in 'screen_width'
    print(f"{dashes}")                              # Prints dashes
    print(f"{output}")                              # Prints output message


def completed():
    dashes = "-" * screen_width                     # Sets dashes to the length specified in 'screen_width'
    print(f"\nOperation completed")                 # Prints message to user
    print(f"{dashes}")                              # Prints dashes


def error(msg): `
    print(f"Error! {msg}\n")


def menu():
    print(f""" Please select one of these options:    
    {"[years]":<10}  List unique years
    {"[tally]":<10}  Tally up medals
    {"[ctally]":<10}  Tally up medals for each team
    {"[exit]":<10}  Exit the program)\n
    """)

    print("Your selection: ", end="")                           # Prints message to user
    selection = input()                                         # Input for user's menu selection
    return selection.strip().lower()                            # Returns the user input


def display_medal_tally(tally):
    print(f"| {'Gold':<10} | {tally['Gold']:<10} |")            # Displays the keys (medal names) and values (medal counts)
    print(f"| {'Silver':<10} | {tally['Silver']:<10} |")        # :<10 aligns text with <10 characters to the left and pads(fills) the rest with spaces
    print(f"| {'Bronze':<10} | {tally['Bronze']:<10} |")


def display_medal_tally(team_tally):
    for key, value in team_tally.items():                       # For each item (key-value pair) in 'team_tally'
        print(key)                                              # Print the key
        print(f"\t{value}")                                     # Print the corresponding value (key and value = items)


def display_years(years):
    for key in sorted(years, reverse=True):                     # Sorts the key called 'years' in reverse order (largest first)
        print(f"{key}")

