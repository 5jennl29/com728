import database

def menu():
    print("Please select one of the following options:\n"
          "[1] Display stock levels\n")

    print("Your selection: ", end="")
    selection = int(input())
    return selection


def run():
    selection = menu()

    if selection == 1:
        database.display_products_with_stock_levels()


if __name__ == "__main__":
    run()