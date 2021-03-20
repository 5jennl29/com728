
def pattern():
    data = {"Short Sequence":3, "Medium Sequence":2, "Long Sequence":1}          # This is the content of the dictionary
    return data                                                                  # Returns the dictionary


def display_keys(data):
    print("Keys:")
    for key in data.keys():                         # For each key in 'data' dictionary
        print(f"{key}")                             # Print the key
    print()                                         # Line space after all keys are printed


def display_values(data):
    print("Values:")
    for value in data.values():                     # For each value in 'data' dictionary
        print(f"{value}")                           # Print that value
    print()


def display_items(data):
    print("Key-Value pairs:")
    for key, value in data.items():                 # For each key-value pair (item) in 'data' dictionary
        print(f"{key}: {value}")                    # Print the key and the corresponding value
    print()


def run():
    data = pattern()                # Calls the function 'pattern' and assigns the returned dictionary to 'data'
    print("Dictionary:")
    print(f"{data}")                # Prints the dictionary content
    print()


    display_keys(data)              # Calls the display functions above with 'data' as the parameter
    display_values(data)
    display_items(data)


# call the function when the module is executed directly
if __name__ == "__main__":
    run()
