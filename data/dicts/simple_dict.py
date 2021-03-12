
def pattern():
    sequences = {"Short Sequence":3, "Medium Sequence":2, "Long Sequence":1}          # This is the content of the dictionary
    return sequences                                                                  # Returns the dictionary


def run():
    pattern_dict = pattern()                # Calls the function 'pattern' and assigns the returned dictionary to 'pattern_dict'
    print(pattern_dict)                     # Prints the dictionary content


# call the function when the module is executed directly
if __name__ == "__main__":
    run()
