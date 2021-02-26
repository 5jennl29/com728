def search(file_path):
    print("Searching...")

    sections = ""       # Variable for sections (empty to start with)
    books = "Books:\n"  # Variable for books (Includes header text for that list)

    with open(file_path) as file:           # Opens the text file, and closes after it's used it
        for line in file:                   # For each line in the file
            if line.startswith("Section"):  # If the line starts with 'section'
                sections += line            # Add it to the variable 'sections'
            else:
                books += line               # Otherwise add it to the variable 'books'

    print("Done!")
    return f"{sections}\n\n{books}"         # Returns the list of sections and the list of books


def save(file_path,data):
    print("Saving...")

    with open(file_path, "w") as file:     # Opens the file in 'write mode' shown by the 'w'
        file.write(data)                   # Writes the variable 'data' to the file

    print("Done!")


def run():
    data = search("books.txt")             # Saves the data returned from the search function in to a variable called 'data' and calls it with the txt file
    save("books.txt", data)            # Calls the save function with the required parameters

run()

