
def likelihood():                               # Likelihood function
    likelihoods = (50, 38, 27, 99, 4)           # Created 'likelihood' variable as a tuple
    return min(likelihoods)                     # Returning the minimum value in tuple 'likelihoods'

def run():                                          # Run function
    min_like = likelihood()                         # Variable for returned value from 'likelihood' function
    print(f"Minimum likelihood of falling: {min_like}%")        # prints result


if __name__ == "__main__":
    run()