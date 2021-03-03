import json  # Imports the json module


def read(file_path):              # Defines the 'read' function
    print("Reading... ", end="")

    with open(file_path) as file:       # Opens the file to be read (which is the default, no need to specify mode)
        data = json.load(file)          # Loads the file content as 'data' variable
        print("Done!")
        return data                     # Returns the loaded 'data' variable


def save(export_file, data):              # Defines the 'save' function
    print("Exporting... ", end="")
    with open(export_file, "w") as file:       # Opens the file in "w" mode (write mode)
        json.dump(data, file, indent=3)        # Saves the data to a file, you can include a specific number of spaces for the indent if required
        print("Done!")


def run():
    json_data = read("robocity.json")      # Reads the file in the parameter and stores the returned 'data' to variable called 'json_data'
    save("exported.json", json_data)       # Writes that data to a file specified as 'exported.json'


if __name__ == "__main__":
  run()