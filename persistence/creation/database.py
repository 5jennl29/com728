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
    print(f"There are {num_records} presenters in total.\n")

    for record in records:
        first_name = record[0]
        last_name = record[1]
        organisation = record[2]

        print(f"Presenter: {first_name} {last_name}, Organisation: {organisation}")

    print("\nOperation completed")


def events_with_locations():
    # CONNECT to database, create cursor object
    db = sqlite3.connect("cbbc_events.db")
    cursor = db.cursor()

    sql = "SELECT event_name, city, country " \
          "FROM event " \
          "INNER JOIN presenter_org ON event.loc_id = presenter_org.loc_id " \
          "INNER JOIN location ON presenter_org.loc_id = location.loc_id; "
    cursor.execute(sql)

    # Method 'fetchall' gets all records from the db
    records = cursor.fetchall()
    db.close()

    for record in records:
        event_name = record[0]
        city = record[1]
        country = record[2]

        print(f"Event: {event_name}, Location: {city}, {country}")

    print("\nOperation completed")


def presenters_at_event(event_id):
    # CONNECT to database, create cursor object
    db = sqlite3.connect("cbbc_events.db")
    cursor = db.cursor()

    sql = "SELECT event.event_name, presenter.first_name, presenter.last_name " \
          "FROM event " \
          "INNER JOIN event_presenter ON event.event_id = event_presenter.event_id " \
          "INNER JOIN presenter ON event_presenter.pres_id = presenter.pres_id" \
          f"WHERE event.id = {event_id}; "
    cursor.execute(sql)

    # Method 'fetchall' gets all records from the db
    records = cursor.fetchall()
    db.close()

    print("Please enter the event id:")
    selection = int(input())

    event_name = set()
    event = []

    for record in records:

        event_id = record[0]
        name_event = record[1]
        name = record[2], record[3]

        if selection == 1 and event_id == 1:
            event_name.add(name_event)
            event.append(name)
        elif selection == 2 and event_id == 2:
            event_name.add(name_event)
            event.append(name)
        elif selection == 3 and event_id == 3:
            event_name.add(name_event)
            event.append(name)
        elif selection == 4 and event_id == 4:
            event_name.add(name_event)
            event.append(name)
        elif selection == 5 and event_id == 5:
            event_name.add(name_event)
            event.append(name)
        else:
            continue

    if selection == 1:
        for _ in event_name:
            print("\nThe event is:")
            print(*event_name)
            print(f"\nThe presenters are: ")
            for item in event:
                print(*item)
    elif selection == 2:
        print("\nThe event is:")
        print(*event_name)
        print(f"\nThe presenters are: ")
        for item in event:
            print(*item)
    elif selection == 3:
        print("\nThe event is:")
        print(*event_name)
        print(f"\nThe presenters are: ")
        for item in event:
            print(*item)
    elif selection == 4:
        print("\nThe event is:")
        print(*event_name)
        print(f"\nThe presenters are: ")
        for item in event:
            print(*item)
    elif selection == 5:
        print("\nThe event is:")
        print(*event_name)
        print(f"\nThe presenters are: ")
        for item in event:
            print(*item)
    else:
        print("Error!")

    print("\nOperation completed")



def events_for_presenter():
    # CONNECT to database, create cursor object
    db = sqlite3.connect("cbbc_events.db")
    cursor = db.cursor()

    sql = "SELECT presenter.pres_id, presenter.first_name, presenter.last_name, event.event_id, event.event_name " \
          "FROM presenter " \
          "INNER JOIN event_presenter ON presenter.pres_id = event_presenter.pres_id " \
          "INNER JOIN event ON event_presenter.event_id = event.event_id ; "
    cursor.execute(sql)

    # Method 'fetchall' gets all records from the db
    records = cursor.fetchall()
    db.close()

    print("Please enter the presenter id (1 -5):")
    selection = int(input())
    event_name = []
    presenter = set()

    for record in records:

        pres_id = record[0]
        name_event = record[4]
        pres_name = record[1], record[2]

        if selection == 1 and pres_id == 1:
            event_name.append(name_event)
            presenter.add(pres_name)
        elif selection == 2 and pres_id == 2:
            event_name.append(name_event)
            presenter.add(pres_name)
        elif selection == 3 and pres_id == 3:
            event_name.append(name_event)
            presenter.add(pres_name)
        elif selection == 4 and pres_id == 4:
            event_name.append(name_event)
            presenter.add(pres_name)
        elif selection == 5 and pres_id == 5:
            event_name.append(name_event)
            presenter.add(pres_name)
        else:
            continue

    if selection == 1:
        print(presenter)
        print("is presenting at: ")
        for event in event_name:
            print(event)
    elif selection == 2:
        print(presenter)
        print("is presenting at: ")
        for event in event_name:
            print(event)
    elif selection == 3:
        print(presenter)
        print("is presenting at: ")
        for event in event_name:
            print(event)
    elif selection == 4:
        print(presenter)
        print("is presenting at: ")
        for event in event_name:
            print(event)
    elif selection == 5:
        print(presenter)
        print("is presenting at: ")
        for event in event_name:
            print(event)
    else:
        print("Error!")

    print("\nOperation completed")