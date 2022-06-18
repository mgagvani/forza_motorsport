# Program to visualize x, y, and z data from FH5 Telemetry

import numpy as np
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt

# Read data
data = np.genfromtxt("forza_data2.csv", dtype=float, delimiter=',', names=True) 
x = data["position_x"]
y = data["position_y"]
z = data["position_z"]


# Create figure
fig = plt.figure()
ax = plt.axes(projection="3d")
ax.plot3D(x, z, y, 'gray')

plt.show()