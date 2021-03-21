import sqlite3                                         # Imports SQLite


def retrieve_bot():
    db = sqlite3.connect("bots.db")                     # Connects to the database 'bots.db'
    cursor = db.cursor()

    sql = "SELECT * FROM bots;"                         # This takes the SQLite query to be executed as a parameter (string) value.
    cursor.execute(sql)                                 # Cursor is used to query the database

    record = cursor.fetchone()                          # Method 'fetchone' gets a single record from the db
    db.close()

    print(record)


def run():
    retrieve_bot()


if __name__ == "__main__":
    run()

