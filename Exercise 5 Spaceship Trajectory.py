import math
import numpy
import matplotlib.pyplot

G = 6.67e-11 # N m2 / kg2

print("This program plots the orbital trajectory/trajectories of a satellite around a massive body.")
earth_mass = float(input("Please enter a value for the size of the massive body. For reference, 5.97e24 is the mass of the Earth. "))
      
def acceleration(spaceship_position):
      vector_to_earth = - spaceship_position
      return G * (earth_mass/(numpy.linalg.norm(vector_to_earth) ** 3)) * vector_to_earth

def ship_trajectory():
      h = float(input("Please enter a value, in seconds, for the size of the timesteps used. 1 is the suggested value. "))
      num_steps = int(input("Please enter an integer value for the number of steps to simulate. 13000 is the suggested value. \
Higher values increase fidelity, lower values decrease fidelity. "))

      x = numpy.zeros([num_steps + 1, 2]) # m
      v = numpy.zeros([num_steps + 1, 2]) # m / s

      x[0, 0] = float(input("Please enter a value for the initial x displacement of the satellite from the massive body. \
For a body of comparable mass with Earth (i.e ~5.97e24), a value around 15e6 is suggested. "))
      # Initial x position
      x[0, 1] = float(input("Please enter a value for the initial y displacement of the satellite from the massive body. \
For a body of comparable mass with Earth (i.e ~5.97e24), a value around 1e6 is suggested. "))
      # Initial y position
      v[0, 0] = float(input("Please enter a value for the x component of the initial velocity. \
For a satellite orbiting a body of comparable mass with Earth, a value around 2e3 is suggested. "))
      # Initial x component of velocity
      v[0, 1] = float(input("Please enter a value for the y component of the initial velocity. \
For a satellite orbiting a body of comparable mass with Earth, a value around 4e3 is suggested. "))
      # Initial y component of velocity

      for step in range(num_steps):
          x[step + 1] = x[step] + (h * v[step])
          v[step + 1] = v[step] + (h * acceleration(x[step]))

      return x, v

x, v = ship_trajectory()

def plot_me():
    matplotlib.pyplot.plot(x[:, 0], x[:, 1])
    matplotlib.pyplot.scatter(0, 0)
    matplotlib.pyplot.axis('equal')
    axes = matplotlib.pyplot.gca()
    axes.set_xlabel('Longitudinal position in m')
    axes.set_ylabel('Lateral position in m')
    matplotlib.pyplot.show()
    
plot_me()
