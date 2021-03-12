def observed():
  list_observations = []

  for count in range(5):
    print("Please enter an observation:")
    observations.append(input())

  return list_observations


def remove_observations(list_obs):
    print("Do you wish to remove observations? [Y/N]")
    response = input()
    while response == Y:
        print("Please enter the observation to be removed:")
        obs_to_rem = str(input())
        list_obs.remove(obs_to_rem)


def run():
    observed(list_obs)
    remove_observations(list_obs)
    data = sorted(list_obs)
    print(f"{data}")

run()




