def run():

    # ask user about book cover
    print("What type of cover does the book have?")
    cover = input()

    # If book cover is soft, ask next question...
    if cover == "soft":

        # ask user if book is perfect bound
        print("Is the book perfect bound?")
        binding = input()

        # if book is perfect bound
        if binding == "yes":
            print("Soft cover, perfect bound books are very popular!")
        else:
            print("Soft covers with coils or stitches are great for short books.")

    #any other answer gives this response
    else:
        print("Books with hard covers can be more expensive!")


# call the function when the module is executed directly
if __name__ == "__main__":
    run()