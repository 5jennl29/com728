# Program to show string operators

print("Please enter the number of lives.")
lives = int(input())

print("Please enter the energy level.")
energy = int(input())

print("Please enter the shield level.")
shield = int(input())

print("Health has been set.\n")

#Print Bot data
print(f"Lives:  {'♥' * lives}")
print(f"Lives:  {'♦' * energy}")
print(f"Lives:  {'❂' * shield}")