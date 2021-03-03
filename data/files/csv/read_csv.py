import csv  # Imports the csv reader

def read(file_path):                         # Defines the function
    with open(file_path) as file:           # Opens the csv file to be read
        csv_reader = csv.reader(file)          # Use the method 'reader' of the csv module to read the file
        headings = next(csv_reader)           # Use python function 'next' to return the next item (line) in the file

        print(f"Headings:\n{headings}")         # Prints the headings in the file
        print("\nValues:")

        for values in csv_reader:
            print(f"{values}")                 # Prints the remaining values line by line

def run():
    read("bots.csv")                         # Provides the csv file name to be passed to 'run'

if __name__ == "__main__":
  run()

