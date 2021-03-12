def observed():
  observations = []                         # Creates empty list called 'observations'

  for count in range(7):                    # For count of 7
    print("Please enter an observation:")   # Print this message
    observations.append(input())            # Add the input to list 'observations'

  return observations                       # Return 'observations' list


def run():
  print("Counting observations...")         # Message to user
  observations = observed()                 # Calls the function 'observed' and stores return value in local variable 'observations'

  # populate set
  observations_set = set()                  # Creates empty set 'observations_set'
  for observation in observations:
    data = (observation, observations.count(observation))    # For each 'observation', add it's content and count how many times it's observed and store to variable 'data'
    observations_set.add(data)                               # Add that data to the set 'observations_set'

  # display set
  for data in observations_set:                              # For the data (defined above) in 'observations_set' print what is at index[0], and the count of it index[1]
    print(f"{data[0]} observed {data[1]} times.")


run()