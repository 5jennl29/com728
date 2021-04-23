import matplotlib.pyplot as plt
import random


def data():
    paths = {}

    print("What type of line would you like? (Choose : -- or -)")
    line = input()

    print("What colour would you like to use? (Choose r g or b)")
    colour = input()

    print("What style of marker would you like? (Choose o s or ^)")
    marker = input()

    paths['line']=line
    paths['colour']=colour
    paths['marker']=marker

    return paths


def generate():
    print("How many lines would you like to display?")
    response = int(input())

    for count in range(response):
        values = data()
        x = random.sample(range(1, 100),10)
        y = random.sample(range(1, 100),10)

        format = f"{values['line']}{values['colour']}{values['marker']}"
        plt.plot(x, y, format)

        plt.show()


def run():
    print("Running...")
    generate()
    print("Done!")


run()