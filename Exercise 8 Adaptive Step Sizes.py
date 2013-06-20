import math
import numpy
import matplotlib.pyplot

T = 12500. 
g = 9.81 
earth_mass = 5.97e24
gravitational_constant = 6.67e-11

def acceleration(spaceship_position):
    vector_to_earth = - spaceship_position
    return gravitational_constant * earth_mass / numpy.linalg.norm(vector_to_earth)**3 * vector_to_earth

def orbit():
    x = numpy.zeros(2)
    # Create a two-entry zero array (contains position co-ordinates)
    v = numpy.zeros(2)
    # Create a two-entry velocity array (contains velocity vector components)

    x[0] = 15e6
    # Initial x co-ordinate
    x[1] = 1e6
    # Initial y co-ordinate

    v[0] = 2e3
    # Initial x component of velocity
    v[1] = 4e3
    # Initial y component of velocity

    matplotlib.pyplot.scatter(x[0], x[1], s=4)
    # Plot a single point (defined by the initial x,y position)

    current_time = 0. 
    h = 100. 
    h_new = h 
    tolerance = 5e5

    while current_time < T:
          # While current_time is less than 12500:
          acceleration0 = acceleration(x)
          # The initial acceleration for the timestep is equal to the acceleration associated with the position at that time
          
          xE = x + h * v
          vE = v + h * acceleration0
          # Euler steps
          
          xH = x + h * 0.5 * (v + vE)
          vH = v + h * 0.5 * (acceleration0 + acceleration(xE))
          # Heun steps
          
          x = xH
          v = vH

          matplotlib.pyplot.scatter(x[0], x[1], s = 1)
          # Plot a single point (defined by the x,y position)
          current_time += h
          # Add the step size to the current time

          euler_LTE = numpy.linalg.norm(xE - xH) + (T * numpy.linalg.norm(vE - vH))
          # Compute the Local Truncation Error associated with the given values
          
          h_new = h * (math.sqrt(tolerance/euler_LTE))
          # Assign the new step size to be equal to h * (sqrt(tolerance/euler_LTE)
          
          h = h_new
          # Let h assume the value of the new step size

    matplotlib.pyplot.axis('equal')
    matplotlib.pyplot.scatter(0., 0.) 
    axes = matplotlib.pyplot.gca()
    axes.set_xlabel('Longitudinal position in m')
    axes.set_ylabel('Lateral position in m')
    matplotlib.pyplot.show()
    return x, v

x, v = orbit()
