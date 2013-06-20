import numpy
import math
import matplotlib.pyplot

print("This program generates a graph of the sine and cosine functions.")
def sin_cos():
    print("Larger values improve the accuracy of the graph. \
Enter values <10 to see how small sample sizes decrease the fidelity of the graph. ")
    
    num_points = int(input("Please enter an integer value for the number of times \
you would like to dissect the circle. "))

    x = numpy.zeros(num_points)
    # Generates a 50x1 matrix named 'x' which is filled with zeros
    sin_x = numpy.zeros(num_points)
    # Generates a 50x1 matrix named 'sin_x' which is filled with zeros
    cos_x = numpy.zeros(num_points)
    # Generates a 50x1 matrix named 'cos_x' which is filled with zeros

    for i in range(num_points):
        # For i from 0 -> 50
        x[i] = ((2 * math.pi) * i) / (num_points - 1)
        # The i-th index of x is equal to (2pi * i / 49]
        # As i increases, the value of the expression increases
        # The value of the expression is maximised when i = 49
        # That is, when 2pi is the only remaining term
        # This is desirable for dissecting the circle into discrete radian lengths
        sin_x[i] = math.sin(x[i])
        # The i-th index of sin_x is equal to
        # The sin of the radian value stored in x
        cos_x[i] = math.cos(x[i])
        # The i-th index of cos_x is equal to
        # The cos of the radian value stored in x
    return x, sin_x, cos_x

x, sin_x, cos_x = sin_cos()

def plot_me():
    matplotlib.pyplot.plot(x, sin_x)
    matplotlib.pyplot.plot(x, cos_x)
    matplotlib.pyplot.show()
    
plot_me()
