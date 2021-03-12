
def observed():
  observations = {"Flying Car", "Sky Scraper", "Laser", "Dome", "Sky Scraper", "Laser", "Dome"}     # Set of items called 'observations'
  return observations                                                                               # Returns that set on function call


def run():
    observations = observed()               # Calls the function and stores the returned value into NEW local variable 'observations'
    print(observations)                     # Print the local variable 'observations'


# call the function when the module is executed directly
if __name__ == "__main__":
    run()