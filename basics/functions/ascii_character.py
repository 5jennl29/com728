def run():

    print("Program started!")
    print("Please enter an ASCII code: ", end="")
    code = abs(int(input()))

    if code in range(32,127):
        character = chr(code)
        print(f"The character represented by the ASCII code {code} is {character}")
    else:
        print("That number is not within range :(")

    print("\nProgram ended!")