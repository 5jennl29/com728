def run():

    # Ask user for number of cables
    print("How many live cables must I avoid?")
    live_cables = int(input())

    # Declare a control variable
    removed_cables = 0

    print()

    # live cables loop
    while removed_cables < live_cables:
        print("Avoiding... ", end="")        # end="empty string" will keep next print statement on the same line.
        removed_cables = removed_cables + 1       # this is adding +1 on each loop
        print("Done!",(removed_cables),"live cables avoided.")

    print()
    print("All live cables have been avoided.")

# call the function when the module is executed directly
if __name__ == "__main__":
    run()