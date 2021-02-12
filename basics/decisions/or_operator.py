#Ask for user input - what type of adventure
print("What type of adventure should I have?")
adventure = input()  #type of adventure stored in this variable 'adventure'

#adventure = scary or short
if (adventure == "scary") or (adventure == "short"):
    print("Entering the dark forest!")

#adventure = safe or long
elif (adventure == "safe") or (adventure == "long"):
    print("Taking the safe route!")

#for everything else...
else:
    print("Not sure which route to take.")
