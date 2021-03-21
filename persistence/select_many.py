import sqlite3                                         # Imports SQLite


def retrieve_bot():
    db = sqlite3.connect("bots.db")                    # 'db' is a variable. It's assigned a reference to the database when it connects.
    cursor = db.cursor()                               # 'cursor' is created

    sql = "SELECT * FROM bots;"                        # This takes the SQLite query to be executed as a parameter (string) value.
    cursor.execute(sql)                                # 'cursor' object uses the method 'execute' to query the database

    all_rows = cursor.fetchall()                        # Method 'fetchall' gets all records from the db

    db.close()                                          # Closes the database (IMPORTANT!)

    print("First bot in the system:")
    print(f"{all_rows[0]}\n")
    print("All bots in the system:")
    for row in all_rows:
        print(row)


def run():
    retrieve_bot()


if __name__ == "__main__":
    run()

