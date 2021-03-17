import csv
import process
import tui


def read_data(file_path):                   # Function definition with parameter 'file_path'
    started()                               # Print message
    print(f"Reading data from {file_path}")

    data = []                               # Global variable 'records' = an empty list
    headings = []                           # Global variable 'headings' = an empty list

    with open(file_path) as file:           # Opens the file
        csv_reader = csv.reader(file)       # Reads the file
        headings = next(csv_reader)         # Passes headings to variable 'headings'
        for line in csv_reader:             # For the remaining lines in the file
            data.append(line)               # Add each line to the list 'data'

    completed()
    return data


def run():
    athlete_data = read_data("athlete_events.csv")

    while True:
        selection = tui.menu()
        if selection == "years":
            pass
        elif selection == "tally":
            pass
        elif selection == "team":
            pass
        elif selection == "exit":
            break
        else:
            tui.error("Invalid Selection!")


if __name__ == "__main__":
    run()
