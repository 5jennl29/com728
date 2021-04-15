import csv                                              # Imports the csv reader
import sqlite3                                          # Imports SQLite3


def read_data_file(file_path):
    movie_records = []
    print("Loading data... ")
    # OPEN file, READ lines in file, APPEND each line to list 'movie_records'
    with open(file_path) as file:
        csv_reader = csv.reader(file)
        _headings = next(csv_reader)
        for line in csv_reader:
            movie_records.append(line)
            num_records = len(movie_records)

        print(f"Done!\nSuccessfully loaded {num_records} records.")
    return movie_records


def create_table_movie_title():
    # CONNECT to db
    db = sqlite3.connect("movietest.db")
    cursor = db.cursor()
    # SQL commands
    sql = "CREATE TABLE IF NOT EXISTS movie_title " \
          "(movie_id INTEGER NOT NULL PRIMARY KEY," \
          "movie_name TEXT NOT NULL, " \
          "release_year TEXT NOT NULL, " \
          "rating REAL NOT NULL); "

    cursor.execute(sql)
    # COMMIT CHANGES and CLOSE db
    db.commit()
    db.close()


def create_table_movie_genre():
    # CONNECT to db
    db = sqlite3.connect("movietest.db")
    cursor = db.cursor()
    # SQL commands
    sql = "CREATE TABLE IF NOT EXISTS movie_genre " \
          "(movie_id INTEGER NOT NULL, " \
          "genre_id INTEGER NOT NULL, " \
          "PRIMARY KEY(genre_id, movie_id), " \
          "FOREIGN KEY(movie_id) REFERENCES movie_title(movie_id), " \
          "FOREIGN KEY(genre_id) REFERENCES genre(genre_id)); "

    cursor.execute(sql)
    # COMMIT CHANGES and CLOSE db
    db.commit()
    db.close()


def create_table_genre():
    # CONNECT to db
    db = sqlite3.connect("movietest.db")
    cursor = db.cursor()
    # SQL commands
    sql = "CREATE TABLE IF NOT EXISTS genre " \
          "(genre_id INTEGER NOT NULL," \
          "genre TEXT NOT NULL," \
          "PRIMARY KEY(genre_id AUTOINCREMENT) " \
          "FOREIGN KEY(genre_id) REFERENCES movie_genre(genre_id)); "

    cursor.execute(sql)
    # COMMIT CHANGES and CLOSE db
    db.commit()
    db.close()


def create_table_movie_actor():
    # CONNECT to db
    db = sqlite3.connect("movietest.db")
    cursor = db.cursor()
    # SQL commands
    sql = "CREATE TABLE IF NOT EXISTS movie_actor " \
          "(movie_id INTEGER NOT NULL, " \
          "act_id INTEGER NOT NULL, " \
          "PRIMARY KEY(movie_id, act_id), " \
          "FOREIGN KEY(movie_id) REFERENCES movie_title(movie_id), " \
          "FOREIGN KEY(act_id) REFERENCES actor(act_id)); "

    cursor.execute(sql)
    # COMMIT CHANGES and CLOSE db
    db.commit()
    db.close()


def create_table_actor():
    # CONNECT to db
    db = sqlite3.connect("movietest.db")
    cursor = db.cursor()
    # SQL commands
    sql = "CREATE TABLE IF NOT EXISTS actor " \
          "(act_id INTEGER NOT NULL," \
          "name TEXT NOT NULL," \
          "PRIMARY KEY(act_id AUTOINCREMENT) " \
          "FOREIGN KEY(act_id) REFERENCES movie_actor(act_id)); "

    cursor.execute(sql)
    # COMMIT CHANGES and CLOSE db
    db.commit()
    db.close()


def create_table_movie_location():
    # CONNECT to db
    db = sqlite3.connect("movietest.db")
    cursor = db.cursor()
    # SQL commands
    sql = "CREATE TABLE IF NOT EXISTS movie_location " \
          "(movie_id INTEGER NOT NULL, " \
          "loc_id INTEGER NOT NULL, " \
          "PRIMARY KEY(movie_id, loc_id), " \
          "FOREIGN KEY(movie_id) REFERENCES movie_title(movie_id), " \
          "FOREIGN KEY(loc_id) REFERENCES location(loc_id)); "

    cursor.execute(sql)
    # COMMIT CHANGES and CLOSE db
    db.commit()
    db.close()


def create_table_location():
    # CONNECT to db
    db = sqlite3.connect("movietest.db")
    cursor = db.cursor()
    # SQL commands
    sql = "CREATE TABLE IF NOT EXISTS location " \
          "(loc_id INTEGER NOT NULL," \
          "country TEXT NOT NULL," \
          "PRIMARY KEY(loc_id AUTOINCREMENT) " \
          "FOREIGN KEY(loc_id) REFERENCES movie_location(loc_id)); "

    cursor.execute(sql)
    # COMMIT CHANGES and CLOSE db
    db.commit()
    db.close()


def create_table_movie_director():
    # CONNECT to db
    db = sqlite3.connect("movietest.db")
    cursor = db.cursor()
    # SQL commands
    sql = "CREATE TABLE IF NOT EXISTS movie_director " \
          "(movie_id INTEGER NOT NULL, " \
          "dir_id INTEGER NOT NULL, " \
          "PRIMARY KEY(movie_id, dir_id), " \
          "FOREIGN KEY(movie_id) REFERENCES movie_title(movie_id), " \
          "FOREIGN KEY(dir_id) REFERENCES director(dir_id)); "

    cursor.execute(sql)
    # COMMIT CHANGES and CLOSE db
    db.commit()
    db.close()


def create_table_director():
    # CONNECT to db
    db = sqlite3.connect("movietest.db")
    cursor = db.cursor()
    # SQL commands
    sql = "CREATE TABLE IF NOT EXISTS director " \
          "(dir_id INTEGER NOT NULL," \
          "name TEXT NOT NULL," \
          "PRIMARY KEY(dir_id AUTOINCREMENT) " \
          "FOREIGN KEY(dir_id) REFERENCES movie_director(dir_id)); "

    cursor.execute(sql)
    # COMMIT CHANGES and CLOSE db
    db.commit()
    db.close()


def insert_to_movie_title(movie_records):
    # CONNECT to db
    db = sqlite3.connect("movietest.db")
    cursor = db.cursor()
    # SQL commands
    for item in movie_records:
        sql = "INSERT INTO movie_title " \
              "(movie_id, movie_name, release_year, rating) " \
              "VALUES (?, ?, ?, ?); "

        values = [item[0], item[1], item[3], item[8]]
        cursor.execute(sql, values)
    # COMMIT CHANGES and CLOSE db
    db.commit()
    db.close()


def insert_to_location(movie_records):
    # CONNECT to db
    db = sqlite3.connect("movietest.db")
    cursor = db.cursor()
    # SQL commands
    for item in movie_records:
        country = item[7]
        locations = []
        for value in country.split(","):
            locations.append(value.strip())

        for item in locations:
            sql = "INSERT INTO location " \
                  "(country) " \
                  "VALUES (?); "

            values = [item]
            cursor.execute(sql, values)

    db.commit()
    db.close()


def insert_to_genre(movie_records):
    # CONNECT to db
    db = sqlite3.connect("movietest.db")
    cursor = db.cursor()
    # SQL commands
    for item in movie_records:
        genre = item[4]
        genres = set()
        for value in genre.split(","):
            genres.add(value.strip())

        for item in genres:
            sql = "INSERT INTO genre " \
                  "(genre) " \
                  "VALUES (?); "

            values = [item]
            cursor.execute(sql, values)

    db.commit()
    db.close()


def insert_to_director(movie_records):
    # CONNECT to db
    db = sqlite3.connect("movietest.db")
    cursor = db.cursor()
    # SQL commands
    for item in movie_records:
        director = item[5]
        directors = set()
        for value in director.split(","):
            directors.add(value.strip())

        for item in directors:
            sql = "INSERT INTO director " \
                  "(name) " \
                  "VALUES (?); "

            values = [item]
            cursor.execute(sql, values)

    db.commit()
    db.close()


def insert_to_actor(movie_records):
    # CONNECT to db
    db = sqlite3.connect("movietest.db")
    cursor = db.cursor()
    # SQL commands
    for item in movie_records:
        actor = item[6]
        actors = set()
        for value in actor.split(","):
            actors.add(value.strip())

        for item in actors:
            sql = "INSERT INTO actor " \
                  "(name) " \
                  "VALUES (?); "

            values = [item]
            cursor.execute(sql, values)

    db.commit()
    db.close()


def run():
    print("Please enter a file path:")
    file_path = input()

    movie_records = read_data_file(file_path)

    print("Creating the tables...")
    create_table_movie_title()
    create_table_movie_genre()
    create_table_genre()
    create_table_movie_actor()
    create_table_actor()
    create_table_movie_location()
    create_table_location()
    create_table_movie_director()
    create_table_director()

    print("Adding data...")
    insert_to_movie_title(movie_records)
    insert_to_location(movie_records)
    insert_to_genre(movie_records)

    print("Done! The data has been added")


if __name__ == "__main__":
    run()
