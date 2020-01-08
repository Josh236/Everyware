from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import numpy as np
from extendedtext import myData
import pylab as pl
import scipy as sp



fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

if myData == "Sadness":
    # Make data
    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(0, np.pi, 100)
    x = 10 * np.outer(np.cos(u), np.sin(v))
    y = 10 * np.outer(np.sin(u), np.sin(v))
    z = 10 * np.outer(np.ones(np.size(u)), np.cos(v))
# Plot the surface
    ax.plot_surface(x, y, z, color='b')
    plt.show()

if myData == "Analytical":
    fig = plt.figure()
    ax = plt.axes(projection="3d")

    z_line = np.linspace(0, 15, 1000)
    x_line = np.cos(z_line)
    y_line = np.sin(z_line)
    ax.plot3D(x_line, y_line, z_line, 'gray')

    z_points = 15 * np.random.random(100)
    x_points = np.cos(z_points) + 0.1 * np.random.randn(100)
    y_points = np.sin(z_points) + 0.1 * np.random.randn(100)
    ax.scatter3D(x_points, y_points, z_points, c=z_points, cmap='hsv');

    plt.show()



if myData == "Confused":
    ax = a3.Axes3D(pl.figure())
    for i in range(10000):
        vtx = sp.rand(3,3)
        tri = a3.art3d.Poly3DCollection([vtx])
        tri.set_color(colors.rgb2hex(sp.rand(3)))
        tri.set_edgecolor('k')
        ax.add_collection3d(tri)
    pl.show()

print(myData)

plt.title(myData)
plt.show()
plt.axis('off')

