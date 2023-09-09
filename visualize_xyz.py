# Program to visualize x, y, and z data from FH5 Telemetry

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation
import matplotlib.cm as cm

# Read data
data = np.genfromtxt("forza_data1.csv", dtype=float, delimiter=',', names=True)
x = data["position_x"]
z = data["position_y"]  # y is up in Forza
y = data["position_z"]
speed = data["speed"]
velocity_x = data["velocity_x"]
velocity_z = data["velocity_y"] # y is up in Forza
velocity_y = data["velocity_z"]

# take every 10th data point
dN = 25
x = x[::dN]
y = y[::dN]
z = z[::dN]
speed = speed[::10]
velocity_x = velocity_x[::dN]
velocity_y = velocity_y[::dN]
velocity_z = velocity_z[::dN]

# Create figure and 3D axes
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Initialize quiver plot with empty data
quiver = ax.quiver([], [], [], [], [], [], color='r', length=0.1, normalize=True)
ax.set_xlim(min(x), max(x))
ax.set_ylim(min(y), max(y))
ax.set_zlim(min(z), max(z))

sc = ax.scatter(x[:1], y[:1], z[:1])

# Function to update the quiver plot in each frame
def update(frame):
    global sc
    ax.cla()
    ax.set_title(f"Frame: {frame}"); print(f"Frame: {frame}", end="\r")
    sc = ax.scatter(x[:frame], y[:frame], z[:frame], c=speed[:frame], cmap='jet', s=1)
    quiver = ax.quiver(x[frame], y[frame], z[frame], velocity_x[frame], velocity_y[frame], velocity_z[frame], color='r', length=25, normalize=True)
    return quiver

# Create the animation
ani = FuncAnimation(fig, update, frames=len(x), repeat=False, blit=False, interval=1)

# Add colorbar outside the subplot
cbar = plt.colorbar(sc, label="Speed (m/s)")
# plt.show()
ani.save("viz_forza1.mp4", fps=30, dpi=500)


