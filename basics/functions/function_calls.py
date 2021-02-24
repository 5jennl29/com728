def run():

    # Define first function
    def display_in_box(word):
        dashes = 6 + len(word)
        print("-" * dashes)
        print(f"|  {word}  |")
        print("-" * dashes)
        # Displays user-entered word in a box

    # Define second function
    def display_lower(word):
        print(word.lower())
    # Displays user-entered word in lower-case

    # Define third function
    def display_upper(word):
        print(word.upper())
    # Displays user-entered word in upper-case

    # Define fourth function
    def display_mirror(word):
        string_length = len(word)
        sliced_string = word[string_length::-1]
        print(f"{word} | {sliced_string}")
    # Displays user-entered word and it's reverse

    # Define fifth function
    def repeat(word):
        print("How many times should the word be displayed?")
        word_count = int(input())  # Variable for user input

        for count in range(word_count):

            if word_count % 2 == 0:
                print(word.lower(), end=" ")
                word_count = word_count -1  # Word_count becomes one less each time, therefore alternates between odd and even display type

            else:
                print(word.upper(), end=" ")
                word_count = word_count -1  # Word_count becomes one less each time, therefore alternates between odd and even display type

            # Displays user-entered word a number of times (user input), alternating between upper and lower case


    # Define sixth function
    def start():
        print("Please enter a word to decipher:")
        word = input()

        print("\nPlease enter a number (1 - 5) to run a decryption program.")
        print("1) Display in a box\n2) Display in lower-case\n3) Display in upper-case\n4) Display mirrored\n5) Display repeated")
        response = input()  # Runs whatever program the user determines

        if response == "1":
            display_in_box(word)

        elif response == "2":
            display_lower(word)

        elif response == "3":
            display_upper(word)

        elif response == "4":
            display_mirror(word)

        elif response == "5":
            repeat(word)

        else:
            print("I'm not sure what I should do!")

        return word

    start()

# call the function when the module is executed directly
if __name__ == "__main__":
    run()