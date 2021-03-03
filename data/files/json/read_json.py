def read(file_path):           # Defines function 'read' and the parameter 'file_path'

    import json                         # Imports the json module
    with open(file_path) as file:       # Opens the file
        data = json.load(file)          # Loads the file content as 'data'

        city_name = data["city"]                 # Declares 'city_name' as the variable for the data marked 'city'
        print(f"\nCity Name: {city_name}")

        population = data["population"]                 # Declares 'population' as the variable for that data
        print(f"\nPopulation Size: {population}\n")

        bots = data["bots"]                      # Variable 'bots' for all of the data on each bot
        for bot in bots:                          # For each bot in 'bots'
            bot_name = bot["name"]
            stats = bot["stats"]
            print(f"{bot_name} has the following stats: {stats}")


def run():
    read("robocity.json")                # Calls the function 'read' with the file_name parameter needed


if __name__ == "__main__":            # Executes the function 'run' when the file is executed directly
  run()