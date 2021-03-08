import csv    # Imports the csv reader

records = []  # Global variable 'records' = an empty list
headings = [] # Global variable 'headings' = an empty list

def load_data(file_path):                   # Function definition with parameter 'file_path'
    print("Loading data... ", end="")       # Print message

    with open(file_path) as file:           # Opens the file
        csv_reader = csv.reader(file)       # Reads the file
        headings = next(csv_reader)         # Passes headings to variable 'headings'
        for line in csv_reader:                # For the remaining lines in the file
            records.append(line)             # Add each line to the variable 'records'

        print("Done!")                      # Print message
        return records, headings


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


def display_passenger_names():
    print("The names of the passengers are...\n")
    passenger_names = ""                                            # Variable 'names' = an empty string
    for values in records:                                          # For the values in the list 'records'
        passenger_names += f"{values[3]}\n"                                   # Add the info in the fourth column (index 3) to the variable 'passenger_names' with a new line
    print(f"{passenger_names}")  # print the name info


def display_num_survived():
    num_survived = 0

    for row in records:                                          # For the values in the list 'records'
        survival_status = row[1]                              # Add the info in the second column (index 1) to the variable 'survival status'

        if "1" in survival_status:
            num_survived += 1
        else:
            num_survived += 0                   # Add 0 to 'num_survived'

    print(f"{num_survived} passengers survived.")  # print the number of survivors


def run():
    records = load_data("titanic.csv")            # Provides csv file name to be passed to 'load_data' function
    selected_option = display_menu()
    if selected_option == 1:
        display_passenger_names()
    if selected_option == 2:
        display_num_survived()
    else:
        print("Error! Option not recognised.")


if __name__ == "__main__":
  run()