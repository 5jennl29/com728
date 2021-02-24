def run():

    # Ask user for number of cables
    print("How many cables should I remove?")
    cables_to_remove = int(input())

    # Declare a control variable
    removed_cables = 0

    # Remove cables
    print()

    while removed_cables < cables_to_remove:
        print("Removed cable.")
        removed_cables = removed_cables + 1

# call the function when the module is executed directly
if __name__ == "__main__":
    run()