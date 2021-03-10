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
            num_records = len(records)

        print(f"Done!\nSuccessfully loaded {num_records} records.")                      # Print message
        return records, headings


def display_menu():
    print("""
Please select one of the following options:
[1] Display the names of all passengers
[2] Display the number of passengers that survived
[3] Display the number of passengers per gender
[4] Display the number of passengers per age group
[5] Display the number of survivors per age group
    """)
    response = int(input())
    return response


def display_passenger_names():
    print("The names of the passengers are...\n")
    passenger_names = ""                                            # Variable 'names' = an empty string
    for values in records:                                          # For the values in the list 'records'
        passenger_names += f"{values[3]}\n"                         # Add the info in the fourth column (index 3) to the variable 'passenger_names' with a new line
    print(f"{passenger_names}")  # print the name info


def display_num_survived():
    num_survived = 0

    for record in records:                              # For the record in the list 'records'
        survival_status_str = record[1]                 # Add the info in the second column of records (index 1) to the variable 'survival status'
        survival_status = int(survival_status_str)

        if survival_status == 1:
            num_survived += 1                   # Add 1 to 'num_survived'
        else:
            num_survived += 0                   # Add 0 to 'num_survived'

    print(f"{num_survived} passengers survived.")  # print the number of survivors


def display_passengers_per_gender():
    female = 0
    male = 0

    for record in records:
        gender = record[4]                    # Add the info in the fifth column (index 4) to the variable 'gender'

        if gender == "male":
            male += 1
        elif gender == "female":
            female += 1
        else:
            print("There has been an error!")

    print(f"Females: {female}, males: {male}.")


def display_passengers_per_age_group():

    children = 0
    adults = 0
    elderly = 0

    for record in records:

        if record[5] == "":
            continue
        else:
            age = float(record[5])

            if age < 18:
                children += 1
            elif age < 65:
                adults += 1
            else:
                elderly += 14

    print(f"Children: {children}, adults: {adults}, elderly: {elderly}.")

def display_survivors_per_age_group():

    children = 0
    adults = 0
    elderly = 0
    child_survived = 0
    adult_survived = 0
    elderly_survived = 0

    for record in records:

        if record[5] == "":
            continue
        else:
            age = float(record[5])
            survival_status = int(record[1])

            if age < 18:
                children += 1
                if survival_status == 1:
                    child_survived += 1
            elif age < 65:
                adults += 1
                if survival_status == 1:
                    adult_survived += 1
            else:
                elderly += 1
                if survival_status == 1:
                    elderly_survived += 1

    print(f"Children: {child_survived}/{children}, adults: {adult_survived}/{adults}, elderly: {elderly_survived}/{elderly}.")


def run():
    records = load_data("titanic.csv")            # Provides csv file name to be passed to 'load_data' function
    selected_option = display_menu()
    if selected_option == 1:
        print("You have selected option 1.\n")
        display_passenger_names()
    elif selected_option == 2:
        print("You have selected option 2.\n")
        display_num_survived()
    elif selected_option == 3:
        print("You have selected option 3.\n")
        display_passengers_per_gender()
    elif selected_option == 4:
        print("You have selected option 4.\n")
        display_passengers_per_age_group()
    elif selected_option == 5:
        print("You have selected option 5.\n")
        display_survivors_per_age_group()
    else:
        print("Error! Option not recognised.")


if __name__ == "__main__":
  run()