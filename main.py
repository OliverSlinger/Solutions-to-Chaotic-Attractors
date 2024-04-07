import matplotlib.pyplot as plt
import numpy
#These are libraries that I will be using in the code matplotlib will be used to draw out the graphs while numpy will be used to store the 3d coordinates in arrays


#This is the Lorenz function with the applicable parameters and equation to calculate the Lorenz attractor
def Lorenz(Coordinates, *, a=10, b=28, c=2.667):

  x, y, z = Coordinates
  dx = a*(y - x)
  dy = b*x - y - x*z
  dz = x*y - c*z
  return numpy.array([dx, dy, dz])

#This is the Rossler function with the applicable parameters and equation to calculate the Rossler attractor
def Rossler(Coordinates, *, a=0.15, b=0.2, c=10):
  
  x, y, z = Coordinates
  dx = - y - z
  dy = x + a*y
  dz = b + z*x - c*z
  return numpy.array([dx, dy, dz])

#This is the Aizawa function with the applicable parameters and equation to calculate the Aizawa attractor
def Aizawa(Coordinates, *, a=0.95, b=0.7, c=0.6, d=3.5, e=0.25,f=0.1):
  
  x, y, z = Coordinates
  dx = (z - b) * x - d*y
  dy = d * x + (z - b) * y
  dz = c + a * z -(z**3)/3 - (x**2 + y**2)*(1+e*z) + f*z*x**3
  return numpy.array([dx, dy, dz])

#This function will take in the initial position and the function that will be used to create the coordinates to be used on the graoh
def GraphMaker(Initial,func):
  dt = 0.01
  iterations = 15000
  Coordinates = numpy.empty((iterations + 1, 3))
  Coordinates[0] = Initial 
  for i in range(iterations):
    Coordinates[i + 1] = Coordinates[i] + func(Coordinates[i]) * dt
  return Coordinates


# Plot
#Plots the Lorenz Attractor
ax = plt.figure().add_subplot(projection='3d')
ax.plot(*GraphMaker((0,1,1),Lorenz).T, lw = 0.5, color = "Crimson")
ax.plot(*GraphMaker((1,1,1),Lorenz).T, lw = 0.5, color = "SkyBlue")
ax.set_xlabel("X(t)")
ax.set_ylabel("Y(t)")
ax.set_zlabel("Z(t)")
ax.set_title("Lorenz Attractor")

#Plots the Rossler Attractor
ay = plt.figure().add_subplot(projection='3d')
ay.plot(*GraphMaker((0,1,1),Rossler).T, lw = 0.5, color = "Crimson")
ay.plot(*GraphMaker((1,1,1),Rossler).T, lw = 0.5, color = "SkyBlue")
ay.set_xlabel("X(t)")
ay.set_ylabel("Y(t)")
ay.set_zlabel("Z(t)")
ay.set_title("Rossler Attractor")

#Plots the Aizawa Attractor
az = plt.figure().add_subplot(projection='3d')
az.plot(*GraphMaker((0,1,1),Aizawa).T, lw = 0.5, color = "Crimson")
az.plot(*GraphMaker((1,1,1),Aizawa).T, lw = 0.5, color = "SkyBlue")
az.set_xlabel("X(t)")
az.set_ylabel("Y(t)")
az.set_zlabel("Z(t)")
az.set_title("Aizawa Attractor")

plt.show()
