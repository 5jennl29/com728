def run():

    print()
    print("What phrase do you see?") # Ask user for input (phrase)
    phrase = input()

    print()
    print("Reversing...")
    print("The phrase is: ", end="")

    for position in range(len(phrase) -1, -1, -1): #Finds the position of each character in the phrase, back one step at a time
        print(phrase[position], end="")

# call the function when the module is executed directly
if __name__ == "__main__":
    run()
