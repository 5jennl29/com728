def cwd():
    import os  # Import OS to check current dir
    path = os.getcwd()  # This module displays the path of the current working directory
    print(f"The current working directory is {path}")
    print("The directory contains the following files:")
    for file in os.listdir(path):  # Displays the content of the directory
        print(file)  # Prints that content


def run():  # Defines function 'run'
    print("Processing...")
    cwd()  # Calls the function above 'cwd'

run()  # Function call for 'run'