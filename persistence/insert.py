import sqlite3                                         # Imports SQLite3


def get_bot_from_user():                                # Collects data from user to enter into database
    print("Please enter bot data...")
    print("Bot name:")
    name = input()

    print("Maximum speed of bot:")
    max_speed = int(input())

    print("Maximum strength of bot:")
    max_strength = int(input())

    print("Please enter the date of manufacture:")
    created = input()

    print("Manufacturer ID:")
    manufacturer = int(input())

    print("Thank you")
    return [name, max_speed, max_strength, created, manufacturer]               # Returns these values as a list


def insert_bot_in_db(bot_data):

    db = sqlite3.connect("bots.db")                    # 'db' is a variable. It's assigned a reference to the database when it connects.
    cursor = db.cursor()                               # 'cursor' is created

    sql = "INSERT INTO bots " \
          "(name, max_speed, max_strength, created, manufacturer) " \          # NOTE: standard brackets needed
          "VALUES " \
          f"('{bot_data[0]}', {bot_data[1]}, {bot_data[2]}, '{bot_data[3]}', '{bot_data[4]}');"   # NOTE: standard brackets needed and quotes around string objects

    cursor.execute(sql)                                # 'cursor' object uses the method 'execute' to query the database
    row_id = cursor.lastrowid                           # Variable to collect the row_id of the new item/record
    db.commit()                                         # Commits to db
    db.close()                                          # Closes the database (IMPORTANT!)

    print("The record has been added to the database!")
    print(f"The ID of the new record is: {row_id}")


def run():
    bot_data = get_bot_from_user()                              # Calls the first function and stores the returned data as 'bot_data'
    insert_bot_in_db(bot_data)                                  # Uses 'bot_data' as the parameter for the insert function.


if __name__ == "__main__":
    run()

