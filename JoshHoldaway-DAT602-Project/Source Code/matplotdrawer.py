from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import numpy as np
from extendedtext import myData
import pylab as pl
import scipy as sp
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from matplotlib import cm



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

if myData == "Confident":
    fig = plt.figure(figsize = (10,10))
    ax = fig.gca(projection='3d')
    X, Y, Z = axes3d.get_test_data(0.05)
    ax.plot_surface(X, Y, Z, rstride=8, cstride=8, alpha=0.3)
    cset = ax.contour(X, Y, Z, zdir='z', offset=-100, cmap=cm.coolwarm)
    cset = ax.contour(X, Y, Z, zdir='x', offset=-40, cmap=cm.coolwarm)
    cset = ax.contour(X, Y, Z, zdir='y', offset=40, cmap=cm.coolwarm)

#ax.set_xlabel('X')
#ax.set_xlim(-40, 40)
#ax.set_ylabel('Y')
#ax.set_ylim(-40, 40)
#ax.set_zlabel('Z')
#ax.set_zlim(-100, 100)

    plt.show()

if myData == "Tentative":
    fig = plt.figure()
    ax = Axes3D(fig)
    x = [0,1,1,0]
    y = [0,0,1,1]
    z = [0,1,0,1]
    verts = [list(zip(x,y,z))]
    ax.add_collection3d(Poly3DCollection(verts))
    plt.show()

if myData == "Anger":
    ax = Axes3D(pl.figure())
    for i in range(10000):
        vtx = sp.rand(3,3)
        tri = a3.art3d.Poly3DCollection([vtx])
        tri.set_color(colors.rgb2hex(sp.rand(3)))
        tri.set_edgecolor('k')
        ax.add_collection3d(tri)
        plt.show()

if myData == "Joy":
    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(0, np.pi, 100)
    x = 10 * np.outer(np.cos(u), np.sin(v))
    y = 10 * np.outer(np.sin(u), np.sin(v))
    z = 10 * np.outer(np.ones(np.size(u)), np.cos(v))
    ax.plot_surface(x, y, z, color='r')
    plt.show()
    plt.title("Joy")

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
    plt.title("Analytical")



if myData == "Confused":
    ax = Axes3D(pl.figure())
    for i in range(10000):
        vtx = sp.rand(3,3)
        tri = a3.art3d.Poly3DCollection([vtx])
        tri.set_color(colors.rgb2hex(sp.rand(3)))
        tri.set_edgecolor('k')
        ax.add_collection3d(tri)
    pl.show()
    plt.title("Confused")

print(myData)

plt.title(myData)
plt.show()
plt.axis('off')

