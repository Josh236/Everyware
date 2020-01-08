from mpl_toolkits.mplot3d import a3
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

if myData == "Analytical":



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

