
def likelihood():                                      # Likelihood function
    likelihoods = (50, 38, 27, 99, 4)                  # Created 'likelihood' variable as a tuple
    return min(likelihoods), max(likelihoods)          # Returning the minimum value in tuple 'likelihoods'


def run():                                          # Run function
    probability = likelihood()                      # Variable for returned values from 'likelihood' function
    print(f"Minimum likelihood of falling: {probability[0]}%")        # prints min results at index 0
    print(f"Maximum likelihood of falling: {probability[1]}%")        # prints max results at index 1


if __name__ == "__main__":
    run()