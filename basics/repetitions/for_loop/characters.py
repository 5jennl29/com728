print()
print("What strange markings do you see?")
markings = input() # Variable to store user input

print("\nIdentifying...\n")

for count in range(0, len(markings), 1): # Counts each character in variable 'markings'
    print(f"Index {count}:", markings[count]) # Displays the index position of each character in the variable

print("\nDone!")