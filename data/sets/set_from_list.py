def observed():
  observations = []

  for count in range(7):
    print("Please enter an observation:")
    observations.append(input())

  return observations


def run():
  print("Counting observations...")
  observations = observed()

  # populate set
  observations_set = set()
  for observation in observations:
    data = (observation, observations.count(observation))    # For each 'observation', count how many times it's observed and store to variable 'data'
    observations_set.add(data)                               # Add that data to the set 'observations_set'

  # display set
  for data in observations_set:                              # For the data (defined above) in 'observations_set' print what is at index[0], and the count of it index[1]
    print(f"{data[0]} observed {data[1]} times.")


run()