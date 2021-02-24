def run():

    # Ask user what kind of book
    print("What type of book is this?")
    book_type = input()

    # If statement for type 'adventure'
    if book_type == "Adventure":
        print("\nI like Adventure books!\n")

    # Message
    print("Finished reading book.")

# call the function when the module is executed directly
if __name__ == "__main__":
    run()