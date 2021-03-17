import csv                                  # Import csv module
import process                              # Import file 'process'
import tui                                  # Import file 'tui'



def read_data(file_path):                           # Function definition with parameter 'file_path'
    tui.started(f"Reading data from {file_path}")

    data = []                                       # Global variable 'data' = an empty list
    _headings = []                                  # Global UNUSED variable '_headings' = an empty list

    with open(file_path) as file:                   # Opens the file
        csv_reader = csv.reader(file)               # Reads the file
        _headings = next(csv_reader)                # Passes headings to variable '_headings'
        for line in csv_reader:                     # For the remaining lines in the file
            data.append(line)                       # Add each line to the list 'data'

    tui.completed()
    return data


def run():
    data = read_data("athlete_events.csv")          # Data variable is the result of the call to function 'read_data'

    while True:                                     # Menu selection
        selection = tui.menu()
        if selection == "years":
            process.list_years(data)
        elif selection == "tally":
            process.tally_medals(data)
        elif selection == "ctally":
            process.tally_team_medals(data)
        elif selection == "exit":
            break                                   # Exits (or breaks) the run of the program
        else:
            tui.error("Invalid Selection!")


if __name__ == "__main__":
    run()
