import database


def show_menu():
    print("""\nPlease select an option from the menu below:\n
    [1] Display a list of all presenters with their organisations
    [2] Display a list of all events with their locations
    [3] Display a list of all presenters for a specified event
    [4] Display a list of all events for a specific presenter 
    """)

    response = int(input("Your selection is: "))
    return response



def run():
    response = show_menu()

    if response == 1:
        presenters_with_org()
    elif response == 2:
        events_with_locations()
    elif response == 3:
        presenters_at_event()
    elif response == 4:
        events_for_presenter()
    else:
        print("Error! Please enter a number 1-4")




run()