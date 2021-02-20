

import random as rnd

def run():
    # Ask user for min value
    print("Please enter the minimum value")
    min = int(input())  # Store min value

    # Ask user for max value
    print("Please enter the maximum value")
    max = int(input())  # Store max value

    # Generate and store random value 'number' between min and max
    number = (rnd.randrange(min, max, 1))

    # Ask user for guess
    print(f"I am thinking of a number between {min} and {max}. Can you guess what it is?")

    # Calls game function
    play_guess_the_number(number)

# Decisions here (using variable 'number')
def play_guess_the_number(number):

    guess = int(input())

    if guess == number:
        print("Congratulations! You guessed my number!")

    elif guess > number:
        print("Your guess is too high!")
        print("Guess again")
        play_guess_the_number(number)

    elif guess < number:
        print("Your guess is too low!")
        print("Guess again")
        play_guess_the_number(number)

    else:
        print("Something has gone wrong!")


run()
