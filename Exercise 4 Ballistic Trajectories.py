import math
import numpy
import matplotlib.pyplot

print("This program gives the flight path of a handful of petrol bombs \
with acceleration due to gravity, speed of the petrol bomb, and other values decided by the user.")

def trajectory():
    h = float(input("Please enter a value, in seconds, for the size of the timesteps. Smaller values increase accuracy, \
while increasing the computational cost. .1 is a good choice. "))
    g = float(input("Please enter a value, in m/s^2, for the acceleration due to gravity. 9.81 is the earth's gravity, and 2 gives a gravity similar to the moon. "))
    initial_speed  = float(input("Please enter the speed that the petrol bomb is thrown at. "))

    start_angle = int(input("Please enter the angle that the first petrol bomb is thrown at (>0*). "))
    end_angle = int(input("Please enter the angle that the last petrol bomb is thrown at (<90*). "))
    print("The range from the first angle to the last angle of projection is the range of values which will be tested. ")
    number_angles = int(input("Please enter the number of petrol bombs you would like throw. "))

    num_steps = int(input("Please enter an integer value for the number of steps you would like to simulate. \
Larger values lead to more expansive models. 200 is a good choice. "))

    angles = numpy.linspace(start_angle, end_angle, number_angles)
    # The linspace function (numerical python library) takes a start angle, end angle, and a number of angles as arguments
    # It then divides the space between start_angle and end_angle into a number of points
    acceleration = numpy.array([0., -g])
    # The array function generates a matrix class with entries inside the list (square brackets)
    
    x = numpy.zeros([num_steps + 1, 2])
    # Creates a 31x2 array filled with zeros (one column for each component)
    v = numpy.zeros([num_steps + 1, 2])
    # Creates a 31x2 array filled with zeros (one column for each component)
    
    for angle in angles:
          angle_rad = numpy.radians(angle)
          # Convert the degrees to radians

          x[0, 0], x[0, 1] = 0, 0
          # Set the initial co-ordinates of the projectile to be (0, 0)

          v[0, 0] = initial_speed * math.cos(angle_rad)
          # The below lines provide information on cosine, and the components of the initial vector. Uncomment them to receive more information.
          # print("The cosine of the initial angle ",angle, "is equal to",math.cos(angle_rad))
          # print("When this is scaled by the initial speed, the x component of the initial speed becomes",initial_speed * math.cos(angle_rad))
          # Set the initial x component of velocity
          # To be equal to the initial speed * cosine of the angle of projection

          v[0, 1] = initial_speed * math.sin(angle_rad)
          # The below lines provide information on sine, and the components of the initial vector. Uncomment them to receive more information.
          # print("The sine of the initial angle ",angle, "is equal to",math.sin(angle_rad))
          # print("When this is scaled by the initial speed, the y component of the initial speed becomes",initial_speed * math.sin(angle_rad))
          # Set the initial y component of velocity
          # To be equal to the initial speed * sin of the angle of projection

          # Both of these assignments are parts of decomposing vectors

          for step in range(num_steps):
                # Forward Euler loop
                x[step + 1] = x[step] + (h * v[step])
                v[step + 1] = v[step] + (h * acceleration)
          matplotlib.pyplot.plot(x[:, 0], x[:, 1])

    matplotlib.pyplot.axis('equal')
    axes = matplotlib.pyplot.gca()
    axes.set_xlabel('Horizontal position in m')
    axes.set_ylabel('Vertical position in m')
    matplotlib.pyplot.show()
    return x, v

trajectory()

again = input("Press Y if you would like to run the program again, or any other key to exit. ")

if again == "Y":
    trajectory()
