import csv    # Imports the csv reader


records = []  # Variable 'records' = an empty list
headings = [] # Variable 'headings' = an empty list


def load_data(file_path):                   # Function definition with parameter 'file_path'
    print("Loading data... ", end="")       # Print message

    with open(file_path) as file:           # Opens the file
        csv_reader = csv.reader(file)       # Reads the file
        headings = next(csv_reader)         # Passes headings to variable 'headings'
        for line in csv_reader:                # For the remaining lines in the file
            records.append(line)             # Add each line to the variable 'records'

        print("Done!")                      # Print message
        return records


def run():
    records = load_data("titanic.csv")            # Provides csv file name to be passed to 'load_data' function
    print(f"Successfully loaded {len(records)} records.")


if __name__ == "__main__":
  run()