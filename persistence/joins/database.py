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

    print(f"There are {num_records} products in the catalogue.")
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
    sql = "SELECT product_id, product.name, supplier.sup_name " \
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

    sql = "SELECT product.name, supplier.sup_name, location.city, location.country " \
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

    # LEFT OUTER JOIN product to supplier table, and supplier to location table
    sql = "SELECT product.name, supplier.sup_name, location.city, location.country " \
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


def display_suppliers_missing_products():
    # CONNECT to database, create cursor object
    db = sqlite3.connect("catalogue.db")
    cursor = db.cursor()

    # EMULATE right outer join... supplier to product table (switch from previous, no location)
    sql = "SELECT product.name, supplier.sup_name " \
          "FROM supplier " \
          "LEFT OUTER JOIN product ON supplier.id = product.supplier_id; " \

    cursor.execute(sql)

    # Method 'fetchall' gets all records from the db
    records = cursor.fetchall()
    db.close()

    for record in records:
        print(f"Supplier: {record[1]}, Product: {record[0]}")

    print("\nOperation completed")


def display_missing_data():
    # CONNECT to database, create cursor object
    db = sqlite3.connect("catalogue.db")
    cursor = db.cursor()

    # FULL OUTER JOIN  TOP = product to supplier, includes location
    # BOTTOM = supplier to location, includes product
    sql = "SELECT product.name, supplier.sup_name, location.city, location.country " \
          "FROM product " \
          "LEFT OUTER JOIN supplier ON product.supplier_id = supplier.id " \
          "LEFT OUTER JOIN location ON location.loc_id = supplier.location_id " \
          "UNION " \
          "SELECT product.name, supplier.sup_name, location.city, location.country " \
          "FROM supplier " \
          "LEFT OUTER JOIN product ON supplier.id = product.supplier_id " \
          "LEFT OUTER JOIN location ON location.loc_id = supplier.location_id " \
          "UNION " \
          "SELECT product.name, supplier.sup_name, location.city, location.country " \
          "FROM supplier " \
          "LEFT OUTER JOIN location ON location.loc_id = supplier.location_id " \
          "LEFT OUTER JOIN product ON supplier.id = product.supplier_id " \
          "UNION " \
          "SELECT product.name, supplier.sup_name, location.city, location.country " \
          "FROM location " \
          "LEFT OUTER JOIN supplier ON location.loc_id = supplier.location_id " \
          "LEFT OUTER JOIN product ON supplier.id = product.supplier_id; "

    cursor.execute(sql)
    # Method 'fetchall' gets all records from the db
    records = cursor.fetchall()

    db.close()

    supp_missing_prods = []
    prod_missing_supps = []
    location_missing_supp = []


    for record in records:

        product_name = record[0]
        supplier_name = record[1]
        location = record[2], record[3]

        if supplier_name == None and product_name != None:
            prod_missing_supps.append(product_name)

        elif product_name == None and supplier_name != None:
            supp_missing_prods.append(supplier_name)

        elif location != None and supplier_name == None:
            location_missing_supp.append(location)

        else:
            continue


    print("The following products are missing suppliers:")
    print(f"{prod_missing_supps}\n")
    print("The following suppliers are missing products:")
    print(f"{supp_missing_prods}\n")
    print("The following locations are not associated with a supplier:")
    print(f"{location_missing_supp}")

    print("\nOperation completed")