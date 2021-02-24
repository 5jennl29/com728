def run():
    # The function
    def identify():
        print("What lies before us?")
        response = input()  # Collects user input

        if response.strip().lower() == "a large boulder":  # Decision based on response
            print("It's time to run!")
        else:
            print("We will be fine.")

    # Call function 'identify'
    identify()

# call the function when the module is executed directly
if __name__ == "__main__":
    run()