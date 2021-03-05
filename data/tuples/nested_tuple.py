
def steps():                  # Defines function called 'steps'
    step_list = [             # List of tuples
        ("step 1", 50),
        ("step 2", 38),
        ("step 3", 46),
        ("step 4", 99),
        ("step 5", 4)]
    return step_list            # Returns the list of tuples


def run():                          # Defines run function
    all_steps = steps()             # Creates variable all_steps from return value of 'steps' function
    good_steps = []                 # Empty list for good_steps
    bad_steps = []                  # Empty list for bad_steps
    for step in all_steps:                   # For each 'step' in list 'all steps'
        if step[1] >= 50:                    # If the value at index position[1] is greater than or equal to 50
            bad_steps.append(step)           # Add it to 'bad_steps'
        else:
            good_steps.append(step)          # Otherwise add it to 'good_steps'

    print(f"\nGood steps: {len(good_steps)}, Bad steps: {len(bad_steps)}")    #Print message displaying the number (length of list) of good steps and bad steps
    print(f"\nTry to avoid {bad_steps}")

if __name__ == "__main__":
    run()

