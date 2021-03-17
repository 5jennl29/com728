import tui

year_from_data = 9                                  # Variable to set the data column for 'years' data
medals_from_data = 14                               # Variable to set the data column for 'medals'
teams_from_data = 6                                 # Variable to set the data column for 'teams'


def list_years(data):
    tui.started("Listing years...")                 # Calls function 'started()'

    years = set()                                   # Create empty set called 'years'

    for record in data:
        year = record[year_from_data]               # Variable to store each record (year) in data
        years.add(year)                             # Add that data to the set 'years'

    tui.display_years(years)                        # Calls function in tui file 'display_years' with 'years' at the parameter
    tui.completed()                                 # Calls function in tui file 'completed()'


def tally_medals(data):
    tui.started("Tallying medals...")               # Calls function 'started()' with a message

    tally = {"Gold": 0, "Silver": 0, "Bronze": 0}   # Creates a dictionary called 'tally'

    for record in data:                             # For each record (line) in the data
        medal = record[medals_from_data]            # Variable to store each medal (the record from [medals_from_data] column 14)
        if medal in ("Gold", "Silver", "Bronze"):   # If the content is one of these keys... Gold, Silver, Bronze
            tally[medal] += 1                       # Add one to the tally for that medal type

    tui.display_medal_tally(tally)                  # Calls the display function
    tui.completed()                                 # Calls function 'completed()'


def tally_team_medals(data):
    tui.started("Tallying results for each team")   # Calls function 'started()' with a message

    team_tally = {}                                 # Creates empty dictionary 'team_tally'

    for record in data:                             # For each record (line) in the data
        team_name = record[teams_from_data]         # Variable 'team_name' to store the name data from the record[position]
        medal = record[medals_from_data]            # Variable 'medal' to store the name data from the record[position]

        if medal not in ("Gold", "Silver", "Bronze"):   # If no 'Gold', 'Silver' or 'Bronze' in medal
            continue                                    # Continue to next line

        if team_name in team_tally:                     # If the team name is already in 'team_tally'
            team_tally[team_name][medal] += 1           # Retrieve the nested medals dictionary for that team and increment the count
        else:
            team_tally[team_name] = {"Gold": 0, "Silver": 0, "Bronze": 0}           # Create the [medal] dictionary
            team_tally[team_name][medal] += 1                                       # And increment the count


    tui.display_medal_tally(team_tally)                 # Calls display function
    tui.completed()                                     # Calls function 'completed()' from tui file

