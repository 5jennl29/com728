import sqlite3                                              # Imports SQLite3

def get_bot_id_from_user():
    print("Please enter the ID of the bot to update:")
    bot_id = int(input())
    return bot_id


def display_bot_from_db(bot_id):

    db = sqlite3.connect("bots.db")                         # 'db' is a variable. It's assigned a reference to the database when it connects.
    cursor = db.cursor()                                    # 'cursor' is created

    sql = f"SELECT * FROM bots WHERE bot_id = {bot_id};"    # This takes the SQLite query to be executed as a parameter (string) value.
    cursor.execute(sql)                                     # 'cursor' object uses the method 'execute' to query the database

    result = cursor.fetchone()                              # Fetches one (specified with bot_id) record from the database

    db.close()                                              # Closes the database (IMPORTANT!)

    print("The bot you want to update is:")
    print(f"Bot ID: {result[0]}\nBot Name: {result[1]}\nMax Speed: {result[2]}\nMax Strength: {result[3]}\nCreation date: {result[4]}\nManufacturer: {result[5]}")


def get_bot_details_from_user():
    print("What is the name of the field to be updated?")
    field = input()
    print(f"What is the new value for {field} field?")
    value = input()
    bot_details = [field, value]

    return bot_details


def update_bot_in_db(bot_id, bot_details):

    print(f"The bot you want to update is: {bot_id}")

    db = sqlite3.connect("bots.db")                    # 'db' is a variable. It's assigned a reference to the database when it connects.
    cursor = db.cursor()                               # 'cursor' is created

    sql = f"UPDATE bots SET {bot_details[0]} = {bot_details[1]} WHERE bot_id = {bot_id};" \

    cursor.execute(sql)                                # 'cursor' object uses the method 'execute' to query the database
    db.commit()
    db.close()                                          # Closes the database (IMPORTANT!)

    print("The record has been updated")


def run():
    bot_id = get_bot_id_from_user()
    display_bot_from_db(bot_id)
    bot_details = get_bot_details_from_user()
    update_bot_in_db(bot_id, bot_details)


if __name__ == "__main__":
    run()

