def search(file_name):
    print("Searching...")
    with open(file_name) as file:     # Opens the text file, and closes after it's used it
        for line in file:
            print(f"Looked in {line.strip()}")    # prints the 1st line in the file, with no spaces either side
        print("...Done!")


def run():
    search("library.txt")


if __name__ == "__main__":  # Runs the function 'run' when file is executed directly
    run()