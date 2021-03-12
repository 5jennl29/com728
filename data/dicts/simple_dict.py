
def pattern():
    sequences = {"Short Sequence":3, "Medium Sequence":2, "Long Sequence":1}
    return sequences


def run():
    pattern_dict = pattern()
    print(pattern_dict)


# call the function when the module is executed directly
if __name__ == "__main__":
    run()
