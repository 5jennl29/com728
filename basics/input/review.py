def run():

    print("\n")
    #Background to the project
    print("Beep enjoys gardening. He wants to plant some flowers, but needs to work out the dimensions of his garden first.")
    print("It would be great if you could help him.\n")
    print("Help Beep by typing in the length and width of his garden, in metres.")

    #Length is a float
    print("Length:")
    length = float(input())

    #Width is a float
    print("Width:")
    width = float(input())

    print(f"Beep's garden is {length} metres long and {width} metres wide.")
    #Area calculation
    area = round(length * width, 1)
    print(f"So Beep's garden is {area} square metres.\n")

    #Add flowers to Beep's garden with 3 x user input
    print("Beep wants to put a flower bed at the bottom of his garden. Help him to plant the flowers for it!\n")
    print("Please enter the number of Geraniums (1-10).")
    geranium = int(input())

    print("Please enter the number of Pansies (1-10).")
    pansy = int(input())

    print("Please enter the number of Begonias (1-10).")
    begonia = int(input())

    print("\n")
    print("Beep's garden looks wonderful!")

    #Print Beep's garden art
    print("----------------")
    print(f"|{'✾' * geranium}")
    print(f"|{'✿' * pansy}")
    print(f"|{'❀' * begonia}")
    print(f"|             ")
    print(f"|             ")
    print(f"|             ")
    print(f"|             ")
    print("----------------")

# call the function when the module is executed directly
if __name__ == "__main__":
    run()