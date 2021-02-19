# Define function
def cross_bridge(steps):

    for step in range(steps):  # For each 'step' in the range of 'steps' (3 in first call, 6 in second call)
        print("Crossed step.")   # Print this message

    if steps > 5:   # Print this if steps are greater than 5
        print("The bridge is collapsing!")
    else:
        print("We must keep going!")  # Otherwise print this message


# Function calls
cross_bridge(3)
cross_bridge(6)

