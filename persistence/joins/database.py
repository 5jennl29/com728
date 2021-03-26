import sqlite3

def display_products_with_stock_levels():

    # CONNECT to database, create cursor object
    db = sqlite3.connect("catalogue.db")
    cursor = db.cursor()

    sql = "SELECT product_id, name, description, quantity " \
          "FROM product " \
          "NATURAL JOIN stock "
    cursor.execute(sql)

    # Method 'fetchall' gets all records from the db
    records = cursor.fetchall()
    db.close()

    num_records = len(records)

    print(f"There are {num_records} in the catalogue.")
    print(f"The stock level for each product is as follows:\n")

    for record in records:
        print(f"Product: {record[1]}")
        print(f"Description: {record[2]}")
        print(f"Stock level: {record[3]}\n")

    print("Operation completed")
