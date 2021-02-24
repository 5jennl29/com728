def run():
    # Display ascii robot 'Beep' with input for the eyes.
    print("Hello, my name is Beep. Please enter a character to represent my eyes.")
    eye = input()

    print("\n")
    print(" (----)")
    print(f"| {eye} {eye}  |")
    print(" (-~--)")
    print("  (--)")
    print(" /    \\")
    print(" (----)\n")
    print("Thank you!")


# call the function when the module is executed directly
if __name__ == "__main__":
    run()
