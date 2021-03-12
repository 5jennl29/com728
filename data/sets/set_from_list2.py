
def observed():
    observations = []                           # This function creates a list of 'observations'
    for count in range(4):                      # For 4 iterations (4 times)
        print("Please enter an observation:")   # It prints this message
        observations.append(input())            # And adds the input (observation) to a list called 'observations'

    return observations                         # It returns that list


def run():
    print("Counting observations...")
    list_obs = observed()                       # Calls the function 'observed' and stores the returned value to variable list_obs

    # Add to set
    set_obs = set()                             # Creates a set
    for value in list_obs:
        data = (value, list_obs.count(value))   # Creates a tuple which is the value from the list, and the number of times it appears in the list)
        set_obs.add(data)                       # Add that data to the set 'set_obs'

    # Display set
    for data in set_obs:                                # For each tuple (value, and count of that value) in set_obs
        print(f"{data[0]} appears {data[1]} times")     # Display the value and the count of it



if __name__ == "__main__":                      # Runs the function 'run' when file is executed directly
    run()

