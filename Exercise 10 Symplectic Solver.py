import math
import numpy
import matplotlib.pyplot

h = 5.0
earth_mass = 5.97e24 
spacecraft_mass = 30000. 
gravitational_constant = 6.67e-11

def acceleration(spaceship_position):
    vector_to_earth = - spaceship_position
    return gravitational_constant * earth_mass / numpy.linalg.norm(vector_to_earth)**3 * vector_to_earth

def symplectic_euler():
    num_steps = 20000
    x = numpy.zeros([num_steps + 1, 2])
    v = numpy.zeros([num_steps + 1, 2]) 
    energy = numpy.zeros(num_steps + 1)

    x[0, 0] = 15e6
    x[0, 1] = 1e6    
    v[0, 0] = 2e3
    v[0, 1] = 4e3

    for step in range(num_steps):
        x[step + 1] = x[step] + h * v[step] 
        v[step + 1] = v[step] + h * acceleration(x[step + 1])

    for step in range(num_steps + 1):
        energy[step] = 0.5 * spacecraft_mass * numpy.linalg.norm(v[step])**2 \
                         - gravitational_constant * earth_mass * spacecraft_mass / numpy.linalg.norm(x[step])

    return x, energy

x, energy = symplectic_euler()

def plot_me():
    axes_positions = matplotlib.pyplot.subplot(211)
    matplotlib.pyplot.plot(x[:, 0], x[:, 1])
    matplotlib.pyplot.scatter(0, 0)
    matplotlib.pyplot.axis('equal')
    axes_positions.set_xlabel('Longitudinal position in m')
    axes_positions.set_ylabel('Lateral position in m')
    axes_energy = matplotlib.pyplot.subplot(212)
    matplotlib.pyplot.plot(energy)
    axes_energy.set_xlabel('Step number')
    axes_energy.set_ylabel('Energy in J')
    matplotlib.pyplot.show()
    
plot_me()
