
def short_pattern():
    pattern = {                                      # Creates dictionary 'pattern'
    "sequence":"101",
    "occurrences":5
    }
    return pattern


def medium_pattern():
    pattern = {                                      # Creates dictionary 'pattern'
    "sequence":"111000",
    "occurrences": 25
    }
    return pattern


def long_pattern():
    pattern = {"sequence":"1100110011001100",        # Creates dictionary 'pattern'
    "occurrences":50
    }
    return pattern


def run():
    print("Analysing patterns...")

    # Creates dictionary 'sequences' which calls and stores the results of the other functions as a 'value' with it's 'key' description.
    sequences = {
        "Short sequence": short_pattern(),
        "Medium sequence": medium_pattern(),
        "Long sequence": long_pattern()
    }
    for key, value in sequences.items():        # For each item (key-value pair) in 'sequences'
        print(f"{key}: {value}")                # Print the key and it's corresponding value


# call the function when the module is executed directly
if __name__ == "__main__":
    run()
