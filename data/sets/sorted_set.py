def observed():
  list_observations = []

  for count in range(5):
    print("Please enter an observation:")
    observation = input()
    list_observations.append(observation)

  return list_observations


def remove_observations(list_obs):
    is_looping = True

    while is_looping:
        print("Do you want to remove an observation? y/n")
        response = input()
        if response.lower() == "y":
            print("Please enter the observation to be removed:")
            obs_to_remove = str(input())
            list_obs.remove(obs_to_remove)
        else:
            is_looping = False



def run():
    list_obs = observed()
    remove_observations(list_obs)

    set_of_data = set()
    for observation in list_obs:
        data = (observation, list_obs.count(observation))       # For each 'observation', count how many times it's observed and store to variable 'data'
        set_of_data.add(data)                                   # Add that data to the set 'data_set'


    for data in sorted(set_of_data):
        print(f"{data[0]} observed {data[1]} times")


run()




