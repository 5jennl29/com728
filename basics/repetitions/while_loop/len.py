def run():

    print() # line space
    print("Please enter a phrase.")  #Request for user input
    user_phrase = input()  #This is the phrase that will determine the number of repetitions

    print(len(user_phrase) * "Bop ") #uses the length (len) of the phrase to determine no. repetitions of the word 'Bop'

# call the function when the module is executed directly
if __name__ == "__main__":
    run()