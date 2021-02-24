def run():

    print("")
    # Background to the problem - sets the scene
    print("Beep doesn't feel quite right, but is not sure what is wrong, or what to do about it.")
    print("Help Beep to determine the problem.\n")

    # Question to user
    print("Do you feel hungry?")
    hunger = input() #user response

    # Question to user
    print("Do you feel tired?")
    tired = input() #user response

    # Decisions based on user responses
    if (hunger == "yes") and (tired == "yes"):
        print("You're hungry and tired. Have some dinner and go to bed!")

    elif (hunger == "yes") and (tired == "no"):
        print("You're hungry. Have some dinner and chill out!")

        # Secondary question to user
        print("Would you like some dinner?")
        dinner = input()

        # Decisions based on user response to secondary (nested) question
        if (dinner == "yes") or (dinner == "maybe"):
            print("Coming right up!")
        else:
            print("No problem.")

    # Decisions based on user responses
    elif (hunger == "no") and (tired == "yes"):
        print("You're tired. Get some rest and go to bed!")

    # Any other answers
    else:
        print("Hmmn, I don't know how to help you :(")

# call the function when the module is executed directly
if __name__ == "__main__":
    run()

