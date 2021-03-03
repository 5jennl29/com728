
def display_chars(file_path, num_char):  # Defines the function with 2 parameters
    with open(file_path) as file:  # Opens the text file, with no need to close it again
        file = file.read(num_char)  # Reads the first specific number of characters on that file
        print(f"\nThe first {num_char} characters are: \n{file}")  # Prints the characters


def display_line(file_path):  # Defines the function with the file path as parameter
    with open(file_path) as file:  # Opens the text file, and closes after it's used it
        line = file.readline().strip(" ")  # Reads the first line of the text file, strips extra spaces
        print(f"\nThe first line is: \n{line}")  # Prints that first line


def display_text(file_path):  # Defines the function with the file path as parameter
    with open(file_path) as file:  # Opens the text file, and closes after it's used it
        file = file.read()  # Reads the whole file
        print(f"\nThe full text is: \n{file}")  # Prints the full text file


def run():
    display_chars("library.txt", 6)  # Calls the function 'display_chars' with the file path and integer for 'num_char' parameter
    display_line("library.txt")  # Calls the function 'display_line'
    display_text("library.txt")  # Calls the function 'display_text'


if __name__ == "__main__":  # Runs the function 'run' when file is executed directly
    run()
