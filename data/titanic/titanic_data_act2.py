import csv    # Imports the csv reader

def load_data(file_path):                   # Function definition with parameter 'file_path'
    print("Loading data... ", end="")       # Print message

    with open(file_path) as file:           # Opens the file
        csv_reader = csv.reader(file)       # Reads the file
        headings = next(csv_reader)         # Passes headings to variable 'headings'
        records = []                       # Variable 'records' = an empty list
        for line in csv_reader:                # For the remaining lines in the file
            records.append(line)             # Add each line to the variable 'records'

        print("Done!")                      # Print message
        return records


def display_menu():
    print("""
Please select one of the following options:
[1] Display the names of all passengers
[2] Display the number of passengers that survived
[3] Display the number of passengers per gender
[4] Display the number of passengers per age group
    """)
    response = int(input())
    return response


def run():
    records = load_data("titanic.csv")            # Provides csv file name to be passed to 'load_data' function
    selected_option = display_menu()
    print(f"You have selected option: {selected_option}")


if __name__ == "__main__":
  run()