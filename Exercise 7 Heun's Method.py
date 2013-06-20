import math
import numpy
import matplotlib.pyplot

total_time = 24. * 3600. 
g = 9.81 
earth_mass = 5.97e24 
gravitational_constant = 6.67e-11 
radius = (gravitational_constant * earth_mass * total_time**2. / 4. / math.pi ** 2.) ** (1. / 3.)
speed = 2.0 * math.pi * radius / total_time

h_array = []
# Initialised empty array for the timestep values
euler_error_array = []
# Initialised empty array for the error values of the Euler method
heuns_error_array = []
# Initialised empty array for the error values of the Heun method

def acceleration(spaceship_position):
    vector_to_earth = - spaceship_position
    return gravitational_constant * earth_mass / numpy.linalg.norm(vector_to_earth)**3 * vector_to_earth

def heuns_method(num_steps):
    h = total_time / num_steps
    # The size of one timestep is equal to the period of one revolution
    # Divided by the number of steps which will be used in the simulation
    # h decreases in size (and so accuracy increases) as the number of steps used is increased

    x = numpy.zeros([num_steps + 1, 2])
    v = numpy.zeros([num_steps + 1, 2]) 

    x[0, 0] = radius
    # The initial x co-ordinate of the spacecraft will be equal to the radius of earth
    v[0, 1] = speed
    # The initial y co=ordinate of the spacecraft's velocity will be equal to 'speed'

    for step in range(num_steps):
          # Forward Euler loop which calculates the values of x and v
          x[step + 1] = x[step] + h * v[step]
          v[step + 1] = v[step] + h * acceleration(x[step])

    error = numpy.linalg.norm(x[-1] - x[0])
    # 'error' is equal to the value of the magnitude of the vector connecting the final index of position
    # (i.e. that value which is closest to the starting position of the spacecraft)
    # To the initial index of position
    # (The distance from the initial position to the final calculated position)
    h_array.append(h)
    # Appends the given value for h to the array containing the values of h
    euler_error_array.append(error)
    # Appends the given value for error to the array containing the values of the errors given by the Euler method

    # Begin Heun's method:
    for step in range(num_steps):
        initial_euler_x = x[step] + h * v[step]
        initial_euler_v = v[step] + h * acceleration(x[step])
        # Initial Euler equations for input into the Heun equations (x subscript E, v subscript E)
        
        x[step + 1] = x[step] + h * ((v[step] + initial_euler_v)/2)
        v[step + 1] = v[step] + h * ((acceleration(x[step]) + acceleration(initial_euler_x))/2)

    error = numpy.linalg.norm(x[-1] - x[0])
    # 'error' is equal to the magnitude of the vector connecting the final index of position
    # (i.e that value which is closest to the starting position of the spacecraft
    # To the initial index of position
    heuns_error_array.append(error)
    # Appends the given value for error to the array containing the values of the errors given by the Heun method
    # The error values for Euler are stored in one array while the error values for Heun are stored in another
    # The plotting operations are handled by matplotlib.pyplot
    
    return x, v, error

for num_steps in [50, 100, 200, 500, 1000]:
    x, v, error = heuns_method(num_steps)

def plot_me():
    matplotlib.pyplot.scatter(h_array, euler_error_array, c = 'g')
    matplotlib.pyplot.scatter(h_array, heuns_error_array, c = 'b')
    matplotlib.pyplot.xlim(xmin = 0.)
    matplotlib.pyplot.ylim(ymin = 0.)
    axes = matplotlib.pyplot.gca()
    axes.set_xlabel('Step size in s')
    axes.set_ylabel('Error in m')
    matplotlib.pyplot.show()
    
plot_me()
