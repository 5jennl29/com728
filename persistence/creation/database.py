import sqlite3


def presenters_with_org():
    # CONNECT to database, create cursor object
    db = sqlite3.connect("cbbc_events.db")
    cursor = db.cursor()

    sql = "SELECT first_name, last_name, org_name " \
          "FROM presenter " \
          "NATURAL JOIN presenter_org; "
    cursor.execute(sql)

    # Method 'fetchall' gets all records from the db
    records = cursor.fetchall()
    db.close()

    num_records = len(records)

    print(f"There are {num_records} presenters.")
    first_name = {record[1]}
    last_name = {record[2]}
    organisation = {record[3]}

    for record in records:
        print(f"Presenter: {first_name}, {last_name}")
        print(f"Organisation: {organisation}")

    print("\nOperation completed")








def events_with_locations():
    pass
def presenters_at_event():
    pass
def events_for_presenter():
    pass