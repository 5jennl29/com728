def started(msg=""):                        # Function definition with parameter
    print(f"--------------------------------------------------------------------------------\nOperation started: {msg}...\n")


def completed():
    print("\nOperation completed.\n--------------------------------------------------------------------------------")


def error(msg):
    print(f"Error! {msg}!")


def menu():
    print("""    
    [years]    List unique years
    [tally]    Tally up medals
    [ctally]   Tally up medals for each team
    [exit]     Exit the program)\n
""")
    print("Your selection:",str(input()))


def display_medal_tally(tally):
    gold_medals = silver_medals = bronze_medals = 0

    if data[14] == "gold":
        gold_medals += 1
    elif data[14] == "silver":
        silver_medals += 1
    elif data[14] == "bronze":
        bronze_medals += 1

    tally = {f"Gold", {gold_medals}, "Silver", {silver_medals}, "Bronze", {bronze_medals}}

    for key, value in tally.items():                      # For each key-value pair (item) in 'tally' dictionary
        print(f"|  {key}: {value}  |")                    # Print the key and the corresponding value

    return gold_medals, silver_medals, bronze_medals


def display_medal_tally(team_tally):

    print("Analysing data...")

    # Creates dictionary 'team_tally' which calls and stores the results of the other functions as a 'value' with it's 'key' description.
    team_tally = {f"{data[6]}": display_medal_tally()}

    for key, value in team_tally.items():        # For each item (key-value pair) in 'team_tally'
        print(f"{key}: {value}")                # Print the key and it's corresponding value


def display_years(years):
    years = set()
    for value in data[9]:
        years = (value)                      # Display each value (year)
        years.add(data)                      # Add that data to the set 'years'


    for data in sorted(years, reverse=True):
        print(f"{years}\n")


def run():
    started(msg)
    completed()
    error(msg)


run()