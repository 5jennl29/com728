# Define first function 'sum_weights'
def sum_weights(beep_weight, bop_weight):
    sum = beep_weight + bop_weight  # Calculations here
    return sum                      # Return value


# Define second function 'calc_ave_weight'
def calc_avg_weight(beep_weight, bop_weight):
    avg_weight = sum_weights(beep_weight, bop_weight) / 2  # Calculations here
    return avg_weight                                      # Return value


# Define third function 'run' for user input
def run():
    print("Please enter Beep's weight:")
    beep_weight = int(input())

    print("Please enter Bop's weight:")
    bop_weight = int(input())

    print("What would you like to calculate (sum or average)?")
    response = input()

# Decide on action and carry it out!
    if response == "sum":
        print("The sum of Beep and Bop's weights is", sum_weights(beep_weight, bop_weight))

    elif response == "average":
        print("The average of Beep and Bop's weights is", calc_avg_weight(beep_weight, bop_weight))

    else:
        print("There has been an error!")


# Run the program
run()