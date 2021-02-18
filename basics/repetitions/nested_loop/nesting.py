print()
print("Please enter a sequence:")  # Ask user for sequence
sequence = input()

print("Please enter the character for the marker:")  # Ask user for marker
marker = input()

# Find markers
marker1_position = -1
marker2_position = -1

for position in range(0, len(sequence), 1):
    character = sequence[position]

    if character == marker:
        if (marker1_position == -1):
            marker1_position = position
        else:
            marker2_position = position

# Display result
print(f"The distance between the markers is {marker2_position - marker1_position - 1}.")