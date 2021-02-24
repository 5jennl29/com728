def run():

    print()
    print("How many mountains should I display?") # Request number of mountains from user
    mountains = int(input()) # Variable to store number of mountains from user input

    for count in range(mountains): # For each count of (mountains) variable, display art below
        print("           __")
        print("          /  \_  ")
        print("         /^    \ ")
        print("        /  ^    \_")
        print("      _/ ^ ^     ^\ ")
        print("     /  ^     ^    \ ")

    print()
    print("Done!") # Loop finished!

# call the function when the module is executed directly
if __name__ == "__main__":
    run()