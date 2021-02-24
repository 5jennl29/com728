def run():

    # Ask user for input 'what did I hear?'
    print("What did I hear?")
    sound = input()

    # Ask user for input 'what did I see?'
    print("What did I see?")
    sight = input()

    # decision with and statement (answers must meet both 'sound' and 'sight' conditions)
    if (sound == "grrr") and (sight == "two red eyes"):
        print("There is a scary creature. I should get out of here!")

    # all other responses/inputs
    else:
        print("I am a little scared but I will continue.")

# call the function when the module is executed directly
if __name__ == "__main__":
    run()
