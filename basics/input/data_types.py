#Code to input various types of data with output being user bmi.

#Name is a string
print("What is your name human?")
name = str(input())
print(f"Nice to meet you {name}")

#Age is an integer
print("How old are you (in years)?")
age = int(input())

#Height is a float
print("How tall are you (in meters)?")
height = float(input())

#Weight is a float
print("How much do you weigh (in kilograms)?")
weight = float(input())

bmi = round(weight / (height ** 2))

print(f"{name} you are {age} years old and your bmi is {bmi}.")