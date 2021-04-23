import matplotlib.pyplot as plt

def display(x_values,y_values):
    plt. xlabel("x values")
    plt. ylabel("y values")

    plt.plot(x_values, y_values, '-r')

    plt.show()


def run():
    x_values = [1,2,3,4,5]
    y_values = [1,4,9,16,25]
    display(x_values,y_values)


run()