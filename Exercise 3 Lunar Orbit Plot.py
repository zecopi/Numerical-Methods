import numpy
import math
import matplotlib.pyplot

print("This program plots the (perfect) circular orbit of a satellite around a central body.")

def orbit():
    satellite_distance = float(input("Please enter a value for the distance of the satellite from the central body, in metres. "))
    
    num_steps = 50

    x = numpy.zeros([num_steps + 1, 2])
    # Creates a 31x2 array, one column represents x distance
    # One column represents y distance
    input_value = numpy.zeros(num_steps)
    # Creates a 50x1 array, with input values (as angles) for sin, cos functions
    
    for i in range(num_steps + 1):
        # For each i between 0 and 50
          input_value = (2 * math.pi * i) / num_steps
          # The angle which will be input to sin and cos
          # It is equal to 2pi * numerator / num steps
          # So that the numerator and num_steps values cancel
          # And 2pi radians is left over as an angle
          # Which maximises the value of the cos and sin functions
          x[i, 0] = satellite_distance * (math.sin(input_value))
          # The x values will be equal to the sin of the input value in radians
          # And then scaled by moon_distance
          x[i, 1] = satellite_distance * (math.cos(input_value))
          # The y values will be equal to the cos of the input value in radians
          # And then scaled by moon_distance
          
    return x

x = orbit()

def plot_me():
    matplotlib.pyplot.axis('equal')
    matplotlib.pyplot.plot(x[:,0], x[:,1])
    axes = matplotlib.pyplot.gca()
    axes.set_xlabel('Longitudinal position in m')
    axes.set_ylabel('Lateral position in m')
    matplotlib.pyplot.show()
    
plot_me()
