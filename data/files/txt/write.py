def search(file_path):
    print("Searching...")

    sections = ""       # Variable for sections (empty to start with)
    books = "Books:\n"  # Variable for books (Includes header text for that list)

    with open(file_path) as file:          # Opens the text file, and closes after it's used it
        for line in file:                  # For each line in the file
            if line.startswith("Section"):  # If the line starts with 'section'
                sections += line      # Add it to the variable 'sections'
            else:
                books += line          # Otherwise add it to the variable 'books'

    print("Done!")
    return f"{sections}\n\n{books}"


def save(file_path,data):
    print("Saving...")

    with open(file_path, "w") as file:
        file.write(data)

    print("Done!")


def run():
    data = search("books.txt")
    save("books.txt", data)

run()

