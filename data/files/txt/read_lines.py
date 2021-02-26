def search(file_name):
    print("Searching...")
    with open(file_name) as file:  # Opens the text file, and closes after it's used it
        for line in file:
            print(f"Looked in {line.strip()}")
        print("...Done!")


def run():
    search("library.txt")


if __name__ == "__main__":  # Runs the function 'run' when file is executed directly
    run()