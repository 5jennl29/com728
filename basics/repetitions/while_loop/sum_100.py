def run():

    print()
    print("Calculating the sum of the first 100 numbers...", end="")

    # control variable
    numb = 1

    # calculation variable
    total = 0

    while numb <= 100:
        total = total + numb
        numb = numb + 1

    print(f" Done! The answer is",total,".")

# call the function when the module is executed directly
if __name__ == "__main__":
    run()
