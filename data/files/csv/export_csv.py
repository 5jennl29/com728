
def export(file_path,num_bots):   # Defines the function
    print("Exporting...")
    import csv                    # Imports csv
    with open(file_path, "a") as file:        # Opens the file in 'append' mode (Add data to the end of file)

        for bot in range(num_bots):           # For all bots in range 'num_bots'
            print("Please enter the bot ID:")
            bot_id = int(input())             # Variable for the bot ID

            print("Please enter the name of the bot:")
            bot_name = str(input())             # Variable for the bot name

            print("Please enter the paint for the bot")
            bot_paint = str(input())             # Variable for the bot paint

            file.write(f"\n{bot_id}, {bot_name}, {bot_paint}")        # Writes those variables to the file

    print("Done!")


def run():                  # Runs the 'export' function with the required parameters
    export("exported_bots.csv", 3)


if __name__ == "__main__":  # This executes the function 'run' when the file is executed directly
    run()