
def likelihood():                                      # Likelihood function
    likelihoods = (50, 38, 27, 99, 4)                  # Created 'likelihood' variable as a tuple
    return min(likelihoods), max(likelihoods)          # Returning the minimum value in tuple 'likelihoods'


def run():                                          # Run function
    min_like = min(likelihood())                    # Variable for returned min value from 'likelihood' function
    max_like = max(likelihood())                    # Variable for returned max value from 'likelihood' function
    print(f"Minimum likelihood of falling: {min_like}%")        # prints results
    print(f"Maximum likelihood of falling: {max_like}%")


if __name__ == "__main__":
    run()