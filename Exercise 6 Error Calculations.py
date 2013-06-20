import math
import numpy
import matplotlib.pyplot

h_array = []
# Initialises an empty array which contains the size of the timesteps
error_array = []
# Initialises an empty array which contains values for the error

total_time = 24. * 3600.
g = 9.81
earth_mass = 5.97e24
gravitational_constant = 6.67e-11
radius = (gravitational_constant * earth_mass * total_time**2. / 4. / math.pi ** 2.) ** (1. / 3.)
speed = 2.0 * math.pi * radius / total_time

def acceleration(spaceship_position):
      # Function which returns an acceleration value given the position of the spaceship
      # The value for spaceship_position is typically given as x[x, y]
      vector_to_earth = - spaceship_position
      return gravitational_constant * earth_mass / numpy.linalg.norm(vector_to_earth)**3 * vector_to_earth

def calculate_error(num_steps):
      # Function to calculate the error

      h = total_time / num_steps
      # The size of one timestep is equal to the period of one revolution
      # Divided by the number of steps which will be used in the simulation
      # h decreases in size (and so accuracy increases) as the number of steps used is increased

      x = numpy.zeros([num_steps + 1, 2])
      # Empty array for the values of displacement, with one column for each component
      v = numpy.zeros([num_steps + 1, 2])
      # Empty array for the values of velocity, with one column for each component

      x[0, 0] = radius
      # The initial x co-ordinate of the spacecraft will be equal to the radius of earth
      v[0, 1] = speed
      # The initial y co=ordinate of the spacecraft's velocity will be equal to 'speed'

      for step in range(num_steps):
            # Forward Euler loop to calculate the values for x and v
            x[step + 1] = x[step] + (h * v[step])
            v[step + 1] = v[step] + (h * acceleration(x[step]))

      error = numpy.linalg.norm(x[-1] - x[0])
      # The value error is equal to the norm/magnitude of the vector connecting the initial position to the last position calculated
      matplotlib.pyplot.scatter(h, error)
      # Matplotlib will plot a graph of h (the size of the timesteps) versus the error in the calculation

      return error
    
for num_steps in [200, 500, 1000, 2000, 5000, 10000]:
      # For loop to calculate the error associated with each value in the list of values for num_steps
      error = calculate_error(num_steps)

def plot_me():
    axes = matplotlib.pyplot.gca()
    axes.set_xlabel('Step size in s')
    axes.set_ylabel('Error in m')
    matplotlib.pyplot.scatter(h_array, error_array)
    matplotlib.pyplot.xlim(xmin = 0.)
    matplotlib.pyplot.ylim(ymin = 0.)
    matplotlib.pyplot.show()

plot_me()
