import csv                                              # Imports the csv reader
import sqlite3                                          # Imports SQLite3

def read_data_file(file_path):
    bot_records = []                                    # Global variable 'bot_records' = an empty list
    print("Loading data... ")                           # Print message

    with open(file_path) as file:                       # Opens the file
        csv_reader = csv.reader(file)                   # Reads the file
        for line in csv_reader:                         # For the remaining lines in the file
            bot_records.append(line)                    # Add each line to the variable 'bot_records'
            num_records = len(bot_records)

        print(f"Done!\nSuccessfully loaded {num_records} records.")      # Print message (tells user number of records)
    return bot_records


def insert_to_db(bot_records):

    db = sqlite3.connect("bots.db")                 # 'db' is a variable. It's assigned a reference to the database when it connects.
    cursor = db.cursor()                            # 'cursor' is created


    for item in bot_records:
        sql = "INSERT INTO bots " \
              "(name, max_speed, max_strength, created, manufacturer) " \
              "VALUES (?, ?, ?, ?, ?);"                                         # Unknown values (from csv file)

        values = [item[0], item[1], item[2], item[3], item[4]]                  # List of values (columns in csv)
        cursor.execute(sql, values)

    db.commit()                                                 # Commit the changes
    db.close()                                                  # Closes the database (IMPORTANT!)



def run():
    print("Please enter a file path:")
    file_path = input()

    bot_records = read_data_file(file_path)

    print("Adding data to the database")
    insert_to_db(bot_records)
    print("Done! The bots have been added to the database")



if __name__ == "__main__":
    run()


