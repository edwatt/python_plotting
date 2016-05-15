from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm   # colour map
import matplotlib.pyplot as plt
import numpy as np          # http://www.numpy.org/
 
ax = Axes3D(plt.figure())
 
#   http://docs.scipy.org/doc/numpy/reference/generated/numpy.arange.html
X = np.arange(-5, 5, 0.25)  # Return evenly spaced values within an interval
Y = np.arange(-5, 5, 0.25)
 
#   http://docs.scipy.org/doc/numpy/reference/generated/numpy.meshgrid.html
X, Y = np.meshgrid(X, Y)    # Return coordinate matrices from coordinate vectors
R = np.sqrt(X**2 + Y**2)    # Square roots of squares
Z = np.sin(R)               # Sine of that.
 
#   http://matplotlib.org/mpl_toolkits/mplot3d/tutorial.html#surface-plots
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.jet)
 
plt.show()
