# Ask user for direction
print("Towards which direction should I paint (up, down, left or right)?")
direction = input()

# Direction decisions
if direction == "up":
    print("I am painting in the upward direction!")

elif direction == "down":
    print("I am painting in the downward direction!")

elif direction == "left":
    print("I am painting in the left direction!")

elif direction == "right":
    print("I am painting in the right direction!")

# any other answer
else:
    print("I have no idea which direction I am painting in!")