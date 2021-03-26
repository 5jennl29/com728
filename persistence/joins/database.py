import sqlite3

def display_products_with_stock_levels():

    # CONNECT to database, create cursor object
    db = sqlite3.connect("catalogue.db")
    cursor = db.cursor()

    sql = "SELECT product_id, name, description, quantity " \
          "FROM product " \
          "NATURAL JOIN stock; "
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

    print("\nOperation completed")


def display_product_supplier():

    # CONNECT to database, create cursor object
    db = sqlite3.connect("catalogue.db")
    cursor = db.cursor()

    # INNER join = intersection between 2 tables
    sql = "SELECT product_id, product.name, supplier.name " \
          "FROM product " \
          "INNER JOIN supplier ON product.supplier_id = supplier.id; "
    cursor.execute(sql)

    # Method 'fetchall' gets all records from the db
    records = cursor.fetchall()
    db.close()

    print("The suppliers for each product are as follows:\n")
    for record in records:
        print(f"Product: {record[1]}, Supplier: {record[2]}")

    print("\nOperation completed")


def display_product_supplier_locations():

    # CONNECT to database, create cursor object
    db = sqlite3.connect("catalogue.db")
    cursor = db.cursor()

    sql = "SELECT product.name, supplier.name, location.city, location.country " \
          "FROM product " \
          "INNER JOIN supplier ON product.supplier_id = supplier.id " \
          "INNER JOIN location ON supplier.location_id = location.loc_id; "

    cursor.execute(sql)

    # Method 'fetchall' gets all records from the db
    records = cursor.fetchall()
    db.close()

    print("The suppliers for each product are as follows:\n")
    for record in records:
        print(f"Product: {record[0]}, Supplier: {record[1]}, Supplier location: {record[2]}, {record[3]}")

    print("\nOperation completed")


def display_products_missing_suppliers():

    # CONNECT to database, create cursor object
    db = sqlite3.connect("catalogue.db")
    cursor = db.cursor()

    sql = "SELECT product.name, supplier.name, location.city, location.country " \
          "FROM product " \
          "LEFT OUTER JOIN supplier ON product.supplier_id = supplier.id " \
          "LEFT OUTER JOIN location ON supplier.location_id = location.loc_id; "

    cursor.execute(sql)

    # Method 'fetchall' gets all records from the db
    records = cursor.fetchall()
    db.close()

    print("The suppliers for each product are as follows:\n")
    for record in records:
        if record[1] == None:
            print(f"Product: {record[0]}, Supplier: {record[1]}")
        else:
            print(f"Product: {record[0]}, Supplier: {record[1]}, Supplier location: {record[2]}, {record[3]}")

    print("\nOperation completed")