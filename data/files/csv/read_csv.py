def run(file_path):                         # Defines the function
    import csv                              # Imports the csv reader
    with open(file_path) as file:           # Opens the csv file to be read
        csv_reader = csv.reader(file)          # Use the method reader of the csv module to read the file
        headings = next(csv_reader)           # Use python function 'next' to return the next item (line) in the file

        print(f"Headings:\n{headings}")         # Prints the headings in the file
        print("Values:")

        for values in csv_reader:
            print(f"{values}")                 # Prints the remaining values line by line


if __name__ == "__main__":
  run("bots.csv")

