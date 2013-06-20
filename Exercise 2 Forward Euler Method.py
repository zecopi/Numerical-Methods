import numpy
import matplotlib.pyplot

print("This program plots a value for height and velocity of a falling object (One-dimensional) with time, using the forward Euler method. ")

def forward_euler():
    h = float(input("Please enter a value for the size of the timesteps, in seconds. \
Smaller timesteps give better accuracy, at the cost of computational expense. "))
    g = float(input("Please enter a value for acceleration due to gravity, in m / s^2. "))
    mass = float(input("Please enter a value for the mass of the falling object, in kg. "))
    num_steps = int(input("Please enter an integer value for the number of steps you would like to model. \
More steps leads to a more expansive model. "))

    t = numpy.zeros(num_steps + 1)
    # Create an array filled with zeros, of size 51. t = this array
    x = numpy.zeros(num_steps + 1)
    # Do the same, and let x = an identical array
    v = numpy.zeros(num_steps + 1)
    # Do the same, and let v = an identical array

    for step in range(num_steps):
        # From 0 to 49:
        t[step + 1] = h * (step + 1)
        # Starting at 1, t takes on the value TIMESTEP * (the loop numerator + 1), or in this example (.1 * (the loop numerator + 1))
        x[step + 1] = x[step] + (h * v[step])
        # Starting at 1, x takes on the value (index of x associated with the loop numerator (i.e initial displacement)
        # + (.1 * index of v associated with the loop numerator (i.e initial velocity)
        v[step + 1] = v[step] - (h * (g * mass))
        # Starting at 1, v takes on the value (index of v associated with the loop numerator (i.e initial velocity)
        # - (.1 * (g * m))
    return t, x, v

t, x, v = forward_euler()

def plot_me():
    axes_height = matplotlib.pyplot.subplot(211)
    matplotlib.pyplot.plot(t, x)
    axes_velocity = matplotlib.pyplot.subplot(212)
    matplotlib.pyplot.plot(t, v)
    axes_height.set_ylabel('Height in m')
    axes_velocity.set_ylabel('Velocity in m/s')
    axes_velocity.set_xlabel('Time in s')
    matplotlib.pyplot.show() 

plot_me()
