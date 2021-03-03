import csv    # Imports the csv reader

def extract(file_path):                # Function definition with parameter 'file_path'
    print("Extracting...", end="")     # Print message

    with open(file_path) as file:      # Opens the file
        csv_reader = csv.reader(file)  # Reads the file
        headings = next(csv_reader)    # Passes headings to unused variable 'headings'
        names = ""                     # Variable 'names' = an empty string
        for values in csv_reader:           # For the remaining values in the file
            names += f"{values[1]}\n"       # Add the info in the second column (index 1) to the variable 'names' with a new line
        print("Done!\nThe extracted names are as follows:")         # Print message
        print(f"{names}")                                           # print the name info


def run():                         # This function calls the 'extract' function with the file path as the parameter
    extract("bots.csv")


if __name__ == "__main__":         # This xecutes the function 'run' when the file is executed directly
  run()

