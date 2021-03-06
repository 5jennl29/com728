import database

def menu():
    print("Please select one of the following options:\n"
          "[1] Display stock levels\n"
          "[2] Display suppliers\n"
          "[3] Display supplier locations\n"
          "[4] Display missing suppliers\n"
          "[5] Display missing products\n"
          "[6] Display missing data\n")

    print("Your selection: ", end="")
    selection = int(input())
    return selection


def run():
    selection = menu()

    if selection == 1:
        database.display_products_with_stock_levels()
    elif selection == 2:
        database.display_product_supplier()
    elif selection == 3:
        database.display_product_supplier_locations()
    elif selection == 4:
        database.display_products_missing_suppliers()
    elif selection == 5:
        database.display_suppliers_missing_products()
    elif selection == 6:
        database.display_missing_data()
    else:
        print("Error! Invalid selection")
        run()


if __name__ == "__main__":
    run()